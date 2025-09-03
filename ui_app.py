import streamlit as st
import pandas as pd
import json
from agentic_ai import agentic_ai_predict
from io import BytesIO
import time

st.set_page_config(
    page_title="Healthcare Agentic AI 🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------- Header -----------------
st.markdown("""
# 🏥 Healthcare Agentic AI 🚀
Predict disease prognosis based on symptoms.
""")

# ----------------- Input Section -----------------
st.subheader("Select Symptoms")
symptoms = [
    "fever", "cough", "fatigue", "headache", "chest_pain",
    "sob", "diarrhea", "nausea", "dizziness", "sore_throat"
]

user_symptoms = {}
cols = st.columns(5)
for idx, symptom in enumerate(symptoms):
    col = cols[idx % 5]
    user_symptoms[symptom] = col.checkbox(symptom.replace("_"," ").title())

# ----------------- Predict Button -----------------
if st.button("🧠 Analyze Patient Data"):
    # Animated pipeline simulation
    pipeline_steps = [
        "✅ Receiving user symptoms...",
        "🧬 Embedding symptoms into vector space...",
        "🔍 Comparing with demo health cases...",
        "🩺 Predicting prognosis using AI model..."
    ]
    placeholder = st.empty()
    for step in pipeline_steps:
        placeholder.markdown(f"**{step}**")
        time.sleep(0.8)  # simulate processing time

    result = agentic_ai_predict(user_symptoms)
    placeholder.empty()

    st.success("Prediction Complete ✅")

    # ----------------- Result Section -----------------
    st.subheader("🩺 Predicted Prognosis")
    st.markdown(f"**{result['predicted_prognosis']}**")
    st.metric("Similarity Score", f"{result['similarity_score']:.2f}")

    # ----------------- Prediction Confidence Bar -----------------
    confidence = result["similarity_score"]
    st.progress(confidence)

    # ----------------- Recommended Next Steps -----------------
    st.subheader("📋 Recommended Next Steps")
    steps = [
        "Consult a healthcare professional for confirmation",
        "Monitor symptoms and vital signs regularly",
        "Consider further diagnostic tests as advised by your doctor",
        "Maintain a healthy lifestyle & follow prescribed medications"
    ]

    step_container = st.container()
    step_container.markdown(
        """
        <div style="background-color:#f0f2f6; padding:15px; border-radius:10px;">
            <ul style="color:#111; font-size:16px;">
                <li>Consult a healthcare professional for confirmation</li>
                <li>Monitor symptoms and vital signs regularly</li>
                <li>Consider further diagnostic tests as advised by your doctor</li>
                <li>Maintain a healthy lifestyle & follow prescribed medications</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ----------------- Download CSV -----------------
    st.subheader("💾 Download Prediction Report")
    df_report = pd.DataFrame({
        "Symptom": list(user_symptoms.keys()),
        "Present": list(user_symptoms.values())
    })
    df_report["Predicted Prognosis"] = result["predicted_prognosis"]
    df_report["Similarity Score"] = result["similarity_score"]

    csv_buffer = BytesIO()
    df_report.to_csv(csv_buffer, index=False)
    csv_bytes = csv_buffer.getvalue()
    st.download_button(
        label="📥 Download CSV",
        data=csv_bytes,
        file_name="prediction_report.csv",
        mime="text/csv"
    )

    st.markdown(
        "Made with ❤️ for hackathon | Powered by FastAPI + TiDB + Agentic AI"
    )
