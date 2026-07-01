import os
import json
import streamlit as st
import time
import base64
from modules.speech_to_text import transcribe_audio
from modules.semantic_eval import calculate_similarity
from modules.audio_utils import extract_audio_features
from modules.scoring_engine import (
    filler_word_ratio,
    evaluate_understanding
)
from modules.waveform import generate_waveform
from modules.report_generator import generate_pdf
import pandas as pd


from database.queries import (
    insert_audio,
    insert_transcript,
    insert_audio_feature,
    insert_similarity,
    insert_evaluation,
    insert_report,
    get_reference_id
)

from modules.gemini_ai import generate_ai_feedback







# ------------------------------------
# Page Configuration
# ------------------------------------
st.set_page_config(
    page_title="Voice-Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 Voice-Based Concept Understanding Analyser")
st.caption("Automated evaluation of spoken conceptual explanations using AI.")
st.divider()

# ------------------------------------
# Sidebar
# ------------------------------------
with st.sidebar:
    logo = base64.b64encode(open("assets/logo.jpeg", "rb").read()).decode()

    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/jpeg;base64,{logo}"
                 style="
                    width:170px;
                    height:170px;
                    border-radius:50%;
                    object-fit:cover;
                    border:4px solid white;
                    box-shadow:0 0 20px rgba(255,255,255,0.35);
                 ">
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.header("About")
    st.write("""
This application evaluates a student's conceptual understanding from spoken audio.

### Technologies Used

- 🎤 OpenAI Whisper
- 🤖 Sentence-BERT
- ✨ Google Gemini AI
- 🎵 Librosa
- 📄 ReportLab
- 🗄 SQL Server
- 📊 Streamlit
""")

# ------------------------------------
# Load Reference Concepts
# ------------------------------------
try:
    with open("reference_data/concepts.json", "r", encoding="utf-8") as file:
        reference_concepts = json.load(file)
except FileNotFoundError:
    st.error("❌ concepts.json not found in reference_data folder.")
    st.stop()
except json.JSONDecodeError:
    st.error("❌ Invalid JSON format in concepts.json.")
    st.stop()

# ------------------------------------
# Upload Section
# ------------------------------------
left, right = st.columns([2, 1])

with left:

    st.subheader("📤 Upload Student Audio")

    audio_file = st.file_uploader(
        "Upload Audio File",
        type=["wav", "mp3", "m4a"]
    )

    selected_topic = st.selectbox(
        "Select Reference Concept",
        list(reference_concepts.keys())
    )

with right:

    st.subheader("📚 Concept Reference")

    st.info(reference_concepts[selected_topic])

st.divider()

# ------------------------------------
# Analyze Button
# ------------------------------------
if st.button("🚀 Analyze"):

    if audio_file is None:
        st.warning("Please upload an audio file.")
        st.stop()

    os.makedirs("audio/input", exist_ok=True)

    audio_path = os.path.join(
        "audio/input",
        audio_file.name
    )

    with open(audio_path, "wb") as f:
        f.write(audio_file.getbuffer())

    st.success("✅ Audio uploaded successfully.")
    st.audio(audio_file)


# ------------------------------------
# Generate and Display Waveform
# ------------------------------------
    os.makedirs("reports/waveform", exist_ok=True)

    waveform_path = "reports/waveform/waveform.png"

    generate_waveform(
        audio_path,
        waveform_path
    )

    st.subheader("🎵 Audio Waveform")
    st.image(waveform_path)


    # ------------------------------------
    # Audio Feature Extraction
    # ------------------------------------
    start = time.time()
    audio_features = extract_audio_features(audio_path)
    end = time.time()
    feature_time = end - start

    st.subheader("🎵 Audio Features")

    st.metric(
    "Feature Extraction Time",
    f"{feature_time:.2f} sec"
    )

    user_id = 1
    ref_concept_id = get_reference_id(selected_topic)
    audio_id = insert_audio(
        user_id,
        audio_file.name,
        audio_path,
        audio_features["duration"],
        "Completed"
    )


    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Duration",
            f"{audio_features['duration']} sec"
        )

    with c2:
        st.metric(
            "Pause Ratio",
            audio_features["pause_ratio"]
        )

    with c3:
        st.metric(
            "RMS Energy",
            audio_features["rms_energy"]
        )


    insert_audio_feature(
        audio_id,
        audio_features["pause_ratio"],
        audio_features["rms_energy"],
        audio_features["duration"]
    )



    
    # ------------------------------------
    # Speech-to-Text
    # ------------------------------------
    start = time.time()
    transcript = transcribe_audio(audio_path)
    end = time.time()
    speech_time = end - start

    st.subheader("📝 Transcript")

    st.metric(
    "Speech-to-Text Time",
    f"{speech_time:.2f} sec"
    )

    transcript_id = insert_transcript(
        audio_id,
        transcript
    )
    if transcript is None:
        st.error("Speech transcription failed.")
        st.stop()




    st.text_area(
        "Recognized Speech",
        transcript,
        height=180
    )

    # ------------------------------------
    # Semantic Similarity
    # ------------------------------------
    reference_text = reference_concepts[selected_topic]

    start = time.time()
    score, level = calculate_similarity(
        transcript,
        reference_text
    )
    end = time.time()
    semantic_time = end - start

    st.subheader("📊 Semantic Evaluation")

    st.metric(
    "Semantic Similarity Time",
    f"{semantic_time:.2f} sec"
    )



    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Similarity Score",
            f"{score}%"
        )

    with col2:
        st.metric(
            "Understanding Level",
            level
        )


    insert_similarity(
        transcript_id,
        ref_concept_id,
        score   
    )
    # ------------------------------------
    # Filler Word Analysis
    # ------------------------------------
    filler_count, total_words, filler_ratio = filler_word_ratio(
        transcript
    )

    st.subheader("💬 Filler Word Analysis")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.metric(
            "Total Words",
            total_words
        )

    with c5:
        st.metric(
            "Filler Words",
            filler_count
        )

    with c6:
        st.metric(
            "Filler Ratio",
            filler_ratio
        )

    # ------------------------------------
    # Final Evaluation
    # ------------------------------------
    final_score, final_level = evaluate_understanding(
        score,
        filler_ratio,
        audio_features
    )
    result_id = insert_evaluation(
        audio_id,
        ref_concept_id,
        final_score,
        final_level,
        "Generated by VBCUA"
    )

    st.subheader("🏆 Final Evaluation")

    st.metric(
        "Overall Score",
        f"{final_score}/100"
    )
    st.progress(final_score / 100)

    st.caption(f"Overall Performance : {final_score}%")





    # ------------------------------------
    # AI Feedback (Gemini)
    # ------------------------------------
    st.subheader("🤖 AI Generated Feedback")

    try:
        with st.spinner("Generating AI Feedback..."):
            ai_feedback = generate_ai_feedback(
                selected_topic,
                transcript
            )

        st.markdown(ai_feedback)

    except Exception as e:
        st.error("Unable to generate AI feedback.")
        st.info(str(e))




# ------------------------------------
# Evaluation Summary Table
# ------------------------------------
    summary = pd.DataFrame({
        "Metric": [
            "Semantic Similarity",
            "Filler Ratio",
            "Pause Ratio",
            "Confidence (Energy)",
            "Final Score",
            "Understanding Level"
        ],
        "Value": [
            f"{score:.2f}%",
            f"{filler_ratio:.3f}",
            f"{audio_features['pause_ratio']:.3f}",
            f"{audio_features['rms_energy']:.4f}",
            f"{final_score}/100",
            str(final_level)
        ]
    })

    st.subheader("📋 Evaluation Summary")
    st.table(summary)


    os.makedirs("reports/pdf", exist_ok=True)

    pdf_path = "reports/pdf/report.pdf"

    start = time.time()
    generate_pdf(
        pdf_path,
        selected_topic,
        transcript,
        waveform_path,
        score,
        filler_ratio,
        audio_features["pause_ratio"],
        audio_features["rms_energy"],
        final_score,
        final_level
    )
    end = time.time()
    pdf_time = end - start
    


    file_size = round(
    os.path.getsize(pdf_path) / 1024,
    2
    )

    insert_report(
        result_id,
        pdf_path,
        file_size
    )
    with open(pdf_path, "rb") as pdf:

        st.download_button(
            "📄 Download PDF Report",
            pdf,
            file_name="Voice_Analysis_Report.pdf",
            mime="application/pdf"
        )

    st.metric(
        "PDF Generation Time",
        f"{pdf_time:.2f} sec"
    )

    if final_score >= 80:
        st.success(final_level)
    elif final_score >= 50:
        st.warning(final_level)
    else:
        st.error(final_level)

    st.balloons()

