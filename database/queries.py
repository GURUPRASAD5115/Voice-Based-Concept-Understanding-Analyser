from database.connection import get_connection


# ------------------------------------
# AUDIO_FILE
# ------------------------------------
def insert_audio(user_id, file_name, file_path, duration, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO AUDIO_FILE
        (user_id,file_name,file_path,duration_sec,status)
        OUTPUT INSERTED.audio_id
        VALUES (?,?,?,?,?)
    """,
    (
        user_id,
        file_name,
        file_path,
        duration,
        status
    ))

    audio_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return audio_id


# ------------------------------------
# TRANSCRIPT
# ------------------------------------
def insert_transcript(audio_id, transcript):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO TRANSCRIPT
        (
            audio_id,
            transcript_text
        )

        OUTPUT INSERTED.transcript_id

        VALUES (?,?)
    """,
    (
        audio_id,
        transcript
    ))

    transcript_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return transcript_id


# ------------------------------------
# AUDIO FEATURE
# ------------------------------------
def insert_audio_feature(
    audio_id,
    pause_ratio,
    rms_energy,
    duration
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO AUDIO_FEATURE
        (
        audio_id,
        pause_ratio,
        rms_energy,
        duration_sec
        )
        VALUES (?,?,?,?)
    """,
    (
        audio_id,
        pause_ratio,
        rms_energy,
        duration
    ))

    conn.commit()
    cursor.close()
    conn.close()


# ------------------------------------
# SEMANTIC SIMILARITY
# ------------------------------------
def insert_similarity(
    transcript_id,
    ref_concept_id,
    similarity
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO SEMANTIC_SIMILARITY
        (
        transcript_id,
        ref_concept_id,
        similarity_score
        )
        VALUES (?,?,?)
    """,
    (
        transcript_id,
        ref_concept_id,
        similarity
    ))

    conn.commit()
    cursor.close()
    conn.close()


# ------------------------------------
# EVALUATION RESULT
# ------------------------------------
def insert_evaluation(
    audio_id,
    ref_concept_id,
    overall_score,
    level,
    notes
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO EVALUATION_RESULT
        (
        audio_id,
        ref_concept_id,
        overall_score,
        understanding_level,
        notes
        )

        OUTPUT INSERTED.result_id

        VALUES
        (?,?,?,?,?)
    """,
    (
        audio_id,
        ref_concept_id,
        overall_score,
        level,
        notes
    ))

    result_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return result_id


# ------------------------------------
# REPORT
# ------------------------------------
def insert_report(
    result_id,
    pdf_path,
    file_size
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO REPORT
        (
        result_id,
        pdf_path,
        file_size_kb
        )
        VALUES
        (?,?,?)
    """,
    (
        result_id,
        pdf_path,
        file_size
    ))

    conn.commit()
    cursor.close()
    conn.close()



def get_reference_id(concept_title):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ref_concept_id
        FROM REFERENCE_CONCEPT
        WHERE concept_title = ?
    """, (concept_title,))

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row:
        return row[0]

    return None