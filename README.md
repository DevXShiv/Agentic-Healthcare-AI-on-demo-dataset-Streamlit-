# Agentic Healthcare AI 🚀

Predict disease prognosis based on symptoms using AI and optional ECG data.  
This project demonstrates an **industry-ready, interactive healthcare AI app** built with **FastAPI**, **Streamlit**, and **TiDB** (demo dataset).

---

## 🔹 Features

- Interactive symptom selection.
- Real-time AI predictions of probable prognosis.
- Confidence bar showing prediction certainty.
- Pipeline visualization: shows step-by-step reasoning for predictions.
- Automatic CSV report download.
- Professional, vibrant UI with animations and emojis.
- Backend powered by agentic AI using a trained symptom model and embedding similarity.

---

## 🖥️ Live Demo

> Currently works on local machine via Streamlit.

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/DevXShiv/Agentic-Healthcare-AI-on-demo-dataset-Streamlit-.git
cd Agentic-Healthcare-AI-on-demo-dataset-Streamlit-
2. Set up Python Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the App
bash
Copy code
streamlit run ui_app.py
📋 How It Works
User selects symptoms (and optionally uploads ECG data).

Backend fetches demo cases from TiDB and computes similarity.

AI predicts prognosis using symptom model.

Pipeline shows step-by-step reasoning:

Encoding symptoms → Computing similarity → Predicting prognosis → Showing confidence

Results displayed with confidence bar, animations, and downloadable CSV.

🎯 Recommended Next Steps (Dynamic per Prediction)
Consult a healthcare professional for confirmation.

Monitor symptoms and vital signs regularly.

Consider further diagnostic tests as advised by your doctor.

Maintain a healthy lifestyle & follow prescribed medications.

📁 Notes for Judges
This project uses a demo dataset. Real clinical deployment requires proper dataset like MIMIC-IV.

The UI and workflow are industry-ready, with professional animations, vibrant layout, and easy-to-follow predictions.

All predictions, pipeline, and confidence visualization are real-time.

💻 Tech Stack
Frontend & UI: Streamlit

Backend: FastAPI, Python

Database: TiDB (demo)

AI: Symptom classification model + embeddings (SentenceTransformer)

Visualization: Plotly, Streamlit charts

📂 Files
ui_app.py → Streamlit UI

agentic_ai.py → Prediction logic

backend/models/ → Trained models (symptom_model.pkl, label_encoder.pkl)

data/ → Demo ECG and symptom data
