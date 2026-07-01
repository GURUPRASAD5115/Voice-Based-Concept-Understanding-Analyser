# 🎤 Voice-Based Concept Understanding Analyser (VBCUA)

## 📌 Overview

The **Voice-Based Concept Understanding Analyser (VBCUA)** is an AI-powered educational assessment platform that evaluates a student's conceptual understanding through spoken explanations.

The application integrates multiple Artificial Intelligence models to automatically transcribe speech, evaluate conceptual understanding, analyze speech quality, generate AI-powered feedback, produce downloadable PDF reports, and store evaluation results in SQL Server.

The system provides an objective and transparent assessment process, making it suitable for students, educators, researchers, and interview preparation.

---

# 🚀 Key Features

- 🎤 Audio Upload & Playback
- 📝 Speech-to-Text using OpenAI Whisper
- 🧠 Semantic Similarity using Sentence-BERT
- ✨ AI Feedback using Google Gemini AI
- 🎵 Audio Feature Extraction (Librosa)
- 💬 Filler Word Detection
- 📊 Overall Understanding Score
- 📈 Performance Metrics
- 📄 PDF Report Generation
- 📉 Audio Waveform Visualization
- 🗄 SQL Server Database Integration
- 🌐 Interactive Streamlit Dashboard

---

# 🤖 AI Technologies Used

| AI Component | Purpose |
|--------------|---------|
| OpenAI Whisper | Speech Recognition |
| Sentence-BERT | Semantic Similarity Evaluation |
| Google Gemini AI | AI-generated Educational Feedback |
| Librosa | Audio Signal Processing |

---

# 🛠 Technology Stack

### Frontend
- Streamlit

### Backend
- Python 3.11

### AI / Machine Learning
- OpenAI Whisper
- Sentence Transformers
- Google Gemini AI
- Librosa

### Database
- Microsoft SQL Server
- PyODBC

### Report Generation
- ReportLab

### Visualization
- Matplotlib

### Libraries
- NumPy
- Pandas
- SoundFile

---

# 📁 Project Structure

```
Smart Bridge Project
│
├── assets
│   ├── logo.jpeg
│   
├── audio
│   ├── input
│   
│
├── database
│   ├── connection.py
│   ├── queries.py
│   └── schema.sql
│
├── modules
│   ├── speech_to_text.py
│   ├── semantic_eval.py
│   ├── audio_utils.py
│   ├── scoring_engine.py
│   ├── waveform.py
│   ├── report_generator.py
│   └── gemini_ai.py
│
├── reference_data
│   └── concepts.json
│
├── reports
│   ├── pdf
│   └── waveform
│
├── tests
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone <repository-url>
cd Smart-Bridge-Project
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Setup

1. Open SQL Server Management Studio (SSMS).

2. Create database

```
VBCUA_DB
```

3. Execute

```
database/schema.sql
```

4. Insert sample records into

- APP_USER
- REFERENCE_CONCEPT

5. Configure

```
database/connection.py
```

with your SQL Server credentials.

---

# ▶ Running the Application

```bash
streamlit run app.py
```

The application launches automatically in your browser.

---

# 🔄 Application Workflow

1. Upload Audio File
2. Play Uploaded Audio
3. Generate Audio Waveform
4. Extract Audio Features
5. Convert Speech to Text
6. Compute Semantic Similarity
7. Detect Filler Words
8. Calculate Final Score
9. Generate AI Feedback (Gemini)
10. Generate PDF Report
11. Store Results in SQL Server

---

# 📊 Performance Monitoring

The application automatically measures:

- Feature Extraction Time
- Speech-to-Text Time
- Semantic Similarity Time
- PDF Generation Time

---

# 📄 Generated Outputs

- Audio Playback
- Audio Waveform
- Speech Transcript
- Semantic Similarity Score
- Audio Feature Metrics
- Filler Word Statistics
- Final Understanding Score
- Progress Bar Visualization
- AI Generated Educational Feedback
- Evaluation Summary Table
- PDF Report
- SQL Server Records

---

# 🗃 Database Tables

- APP_USER
- AUDIO_FILE
- TRANSCRIPT
- AUDIO_FEATURE
- REFERENCE_CONCEPT
- SEMANTIC_SIMILARITY
- EVALUATION_RESULT
- REPORT

---

# 🧪 Testing

The project includes:

- Functional Testing
- Performance Testing
- Database Validation
- End-to-End Testing

Run tests

```bash
python tests/test_audio.py

python tests/test_semantic.py

python tests/test_scoring.py

python tests/test_database.py
```

---

# 📈 Performance Optimization

- Modular architecture
- Fast semantic embedding computation
- Optimized audio processing
- Lightweight Streamlit interface
- Efficient SQL transactions

---

# 🎯 Future Enhancements

- Live Microphone Evaluation
- Multilingual Speech Analysis
- Student Progress Dashboard
- Teacher Analytics Portal
- Cloud Deployment
- Adaptive AI Recommendations

---

# Demo Video Link
      https://drive.google.com/file/d/1mV3SJ5Ps8t0Z34WWfsXiajRBGXyvuRT8/view

# 👨‍💻 Developer

**Rama Guru Prasad**

Bachelor of Technology

Computer Science and Engineering

---

# 📜 License

Developed as part of the **SmartBridge Internship Project** for educational and learning purposes.
