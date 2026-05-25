# 🎓 CareerLens AI

## Intelligent Multimodal Career Recommendation System using Azure AI Services

CareerLens AI is an AI-powered multimodal recommendation system developed for intelligent career guidance. The system accepts multiple forms of input including **text**, **voice**, and **image uploads**, processes them using Azure AI services, and recommends suitable career paths using machine learning techniques.

---

## 📌 Project Features

✅ Text-based career recommendation

✅ Voice input using Azure Speech-to-Text

✅ Resume / certificate image upload

✅ OCR extraction using Azure Computer Vision

✅ Machine learning recommendation engine

✅ Match score generation

✅ Career explanation output

✅ Interactive Streamlit dashboard

---

## 🏗 System Architecture

```text
User Input
(Text / Voice / Image)
            │
            ▼
    Streamlit Interface
            │
            ▼
 ┌───────────────────────┐
 │ Azure Speech Service  │
 │ Speech → Text         │
 └───────────────────────┘
            │
            ▼
 ┌───────────────────────┐
 │ Azure Vision OCR      │
 │ Image → Text          │
 └───────────────────────┘
            │
            ▼
 Data Preprocessing Layer
            │
            ▼
TF-IDF Feature Extraction
            │
            ▼
Cosine Similarity Engine
            │
            ▼
Career Recommendation
            │
            ▼
Result Dashboard
```

---

## 🧠 Technologies Used

### Frontend
- Streamlit

### Backend
- Python
- Pandas
- NumPy

### Machine Learning
- TF-IDF Vectorizer
- Cosine Similarity
- Scikit-learn

### Azure AI Services
- Azure Speech-to-Text
- Azure Computer Vision OCR

---

## 📂 Project Structure

```text
CareerLensAI/
│
├── app.py
│
├── data/
│   └── career_dataset.csv
│
├── model/
│   └── recommender.py
│
├── services/
│   ├── voice_input.py
│   └── image_ocr.py
│
├── screenshots/
│   ├── dashboard.png
│   ├── voice_input.png
│   ├── ocr_output.png
│   └── recommendations.png
│
├── requirements.txt
│
└── README.md
```

---

## 📊 Dataset

Dataset source:

Career Recommendation Dataset (Kaggle)

https://www.kaggle.com/datasets/breejeshdhar/career-recommendation-dataset

Dataset includes:

- Skills
- Academic information
- Certifications
- Career labels
- Student profiles

---

## ⚙ Installation

Clone repository:

```bash
git clone https://github.com/ISHANI723/CareerLensAI.git
```

Move into project:

```bash
cd CareerLensAI
```

Create environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run project:

```bash
streamlit run app.py
```

---

## 🎤 Multimodal Inputs

### Text Input

Users can enter:

- Skills
- Interests
- Technologies
- Certifications

Example:

```text
Python
Machine Learning
Azure
Cloud Computing
```

---

### Voice Input

Users can speak:

```text
I have experience in AI, Python and Data Analytics
```

Azure Speech converts audio into text.

---

### Resume OCR

Users upload:

- Resume images
- Certificates
- Academic transcripts

Azure OCR extracts:

```text
Python
TensorFlow
SQL
Power BI
```

---

## 🏆 Example Output

Career Recommendations:

1. AI Engineer — 91%

2. Data Scientist — 86%

3. Machine Learning Engineer — 81%

Reason:

- Python skills detected
- Machine learning experience found
- Analytics background identified

---

## ☁ Azure Services Used

### Azure Speech Service

Purpose:

Voice recognition and speech-to-text conversion.

### Azure Computer Vision OCR

Purpose:

Extract text from resume and certificate images.

---

## 📄 Academic Submission

This project was developed for:

**SIT788 Engineering AI**

**Intelligent Bot Development**

## 👩‍💻 Author

Name: Ishani Bhongale

University: Deakin University

Unit: SIT788 Engineering AI

Project:

CareerLens AI – Intelligent Multimodal Career Recommendation System

---
