# Functional Testing Report

**Project:** Voice-Based Concept Understanding Analyser (VBCUA)

**Testing Type:** Functional Testing

**Environment**
- Operating System: Windows 11
- IDE: Visual Studio Code
- Framework: Streamlit
- Language: Python 3.11
- Database: Microsoft SQL Server
- AI Models: OpenAI Whisper, Sentence-BERT, Google Gemini AI

---

## Test Case 1

**Feature:** Audio File Upload

**Description:**
Verify that the application accepts supported audio formats.

**Input:**
MachineLearning.mp3

**Expected Result:**
Audio uploads successfully.

**Actual Result:**
Audio uploaded successfully.

**Status:** PASS

---

## Test Case 2

**Feature:** Audio Playback

**Description:**
Verify uploaded audio can be played inside the application.

**Input:**
Uploaded MP3 file

**Expected Result:**
Audio player appears and playback works.

**Actual Result:**
Audio played successfully.

**Status:** PASS

---

## Test Case 3

**Feature:** Waveform Visualization

**Description:**
Verify waveform generation using uploaded audio.

**Input:**
MachineLearning.mp3

**Expected Result:**
Waveform image displayed.

**Actual Result:**
Waveform generated successfully.

**Status:** PASS

---

## Test Case 4

**Feature:** Audio Feature Extraction

**Description:**
Verify extraction of duration, pause ratio and RMS energy.

**Input:**
Uploaded audio

**Expected Result:**
All audio metrics displayed.

**Actual Result:**
Metrics displayed successfully.

**Status:** PASS

---

## Test Case 5

**Feature:** Speech-to-Text Transcription

**Description:**
Verify OpenAI Whisper converts speech into text.

**Input:**
MachineLearning.mp3

**Expected Result:**
Transcript generated.

**Actual Result:**
Transcript displayed successfully.

**Status:** PASS

---

## Test Case 6

**Feature:** Semantic Similarity Evaluation

**Description:**
Verify Sentence-BERT computes similarity with reference concept.

**Input:**
Generated transcript

**Expected Result:**
Similarity score and understanding level displayed.

**Actual Result:**
Similarity calculated successfully.

**Status:** PASS

---

## Test Case 7

**Feature:** Filler Word Analysis

**Description:**
Verify filler word detection.

**Input:**
Generated transcript

**Expected Result:**
Total words, filler count and filler ratio displayed.

**Actual Result:**
Statistics generated successfully.

**Status:** PASS

---

## Test Case 8

**Feature:** Final Evaluation

**Description:**
Verify overall score generation.

**Input:**
Semantic score, filler ratio and audio features

**Expected Result:**
Overall score, progress bar and understanding level displayed.

**Actual Result:**
Evaluation generated successfully.

**Status:** PASS

---

## Test Case 9

**Feature:** AI Feedback Generation

**Description:**
Verify Google Gemini generates educational feedback.

**Input:**
Transcript and selected concept

**Expected Result:**
AI-generated summary, strengths, weaknesses and suggestions displayed.

**Actual Result:**
Feedback generated successfully.

**Status:** PASS

---

## Test Case 10

**Feature:** Performance Monitoring

**Description:**
Verify execution time measurement.

**Input:**
Complete analysis

**Expected Result:**
Execution time displayed for:
- Feature Extraction
- Speech-to-Text
- Semantic Similarity
- PDF Generation

**Actual Result:**
Performance metrics displayed successfully.

**Status:** PASS

---

## Test Case 11

**Feature:** PDF Report Generation

**Description:**
Verify ReportLab generates downloadable report.

**Input:**
Completed evaluation

**Expected Result:**
PDF generated and download button displayed.

**Actual Result:**
PDF downloaded successfully.

**Status:** PASS

---

## Test Case 12

**Feature:** SQL Server Database Storage

**Description:**
Verify all analysis data is stored.

**Input:**
Completed evaluation

**Expected Result:**
Records inserted into database tables.

**Actual Result:**
Records stored successfully.

**Status:** PASS

---

## Test Case 13

**Feature:** Database Validation

**Description:**
Verify stored records using SQL queries.

**Input**

```sql
SELECT * FROM AUDIO_FILE;
SELECT * FROM TRANSCRIPT;
SELECT * FROM AUDIO_FEATURE;
SELECT * FROM SEMANTIC_SIMILARITY;
SELECT * FROM EVALUATION_RESULT;
SELECT * FROM REPORT;
```

**Expected Result:**
All tables contain newly inserted records.

**Actual Result:**
Records verified successfully.

**Status:** PASS

---

# Functional Testing Summary

| Test Case | Feature | Status |
|------------|---------|--------|
| TC-01 | Audio Upload | PASS |
| TC-02 | Audio Playback | PASS |
| TC-03 | Waveform Visualization | PASS |
| TC-04 | Audio Feature Extraction | PASS |
| TC-05 | Speech-to-Text | PASS |
| TC-06 | Semantic Similarity | PASS |
| TC-07 | Filler Word Analysis | PASS |
| TC-08 | Final Evaluation | PASS |
| TC-09 | AI Feedback Generation | PASS |
| TC-10 | Performance Monitoring | PASS |
| TC-11 | PDF Report Generation | PASS |
| TC-12 | Database Storage | PASS |
| TC-13 | Database Validation | PASS |

---

# Overall Result

**Total Test Cases:** 13

**Passed:** 13

**Failed:** 0

**Success Rate:** 100%

**Overall Result:** ✅ **SUCCESS**