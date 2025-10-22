import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# ----------------------------
# ⚙️ Page Config
# ----------------------------
st.set_page_config(page_title="Patient Portal", layout="wide")

st.title("🧑 Patient Portal")
st.caption("For patients to view personal health trends and AI assessments")

# ----------------------------
# 📊 Simulated Health Data
# ----------------------------
@st.cache_data
def health_data():
    dates = pd.date_range(end=datetime.today(), periods=60)
    df = pd.DataFrame({
        "date": dates,
        "systolic_bp": 120 + np.random.randn(60).cumsum(),
        "diastolic_bp": 80 + np.random.randn(60).cumsum(),
        "heart_rate": 70 + np.random.randn(60) * 2
    })
    return df

df = health_data()

# ----------------------------
# 📈 Metric Selection
# ----------------------------
st.subheader("📈 Health Metrics Over Time")

available_metrics = ["systolic_bp", "diastolic_bp", "heart_rate"]
selected_metrics = st.multiselect(
    "Select metrics to visualize",
    options=available_metrics,
    default=["systolic_bp", "diastolic_bp"]
)

if selected_metrics:
    st.line_chart(df.set_index("date")[selected_metrics])
else:
    st.info("Please select at least one metric to display.")

# ----------------------------
# 🧪 Test Results
# ----------------------------
st.subheader("🧪 Test Results")

test_type = st.radio(
    "Select Test Type",
    ["Blood Test", "Urine Test"],
    horizontal=True
)

if test_type == "Blood Test":
    test_results = pd.DataFrame({
        "Parameter": ["Hemoglobin", "WBC Count", "Platelets", "Cholesterol"],
        "Result": ["13.5 g/dL", "6,200 /µL", "250,000 /µL", "180 mg/dL"],
        "Normal Range": ["12–16 g/dL", "4,000–10,000 /µL", "150,000–400,000 /µL", "<200 mg/dL"],
        "Status": ["Normal", "Normal", "Normal", "Normal"]
    })
else:
    test_results = pd.DataFrame({
        "Parameter": ["pH", "Protein", "Glucose", "Ketones"],
        "Result": ["6.5", "Negative", "Negative", "Negative"],
        "Normal Range": ["4.5–8.0", "Negative", "Negative", "Negative"],
        "Status": ["Normal", "Normal", "Normal", "Normal"]
    })

st.table(test_results)

# ----------------------------
# 📅 Upcoming Events
# ----------------------------
st.subheader("📅 Upcoming Events")

upcoming_events = pd.DataFrame({
    "Date": ["2025-03-05", "2025-03-09"],
    "Department": ["Ophthalmology", "Psychology"],
    "Details": [
        "Eye examination @Ottawa Central Hospital",
        "Counseling session with Dr. Lai @155 Daly Ave"
    ]
})

st.table(upcoming_events)

# ----------------------------
# 💊 Historical Prescriptions
# ----------------------------
st.subheader("💊 Historical Prescriptions")

historical_prescriptions = pd.DataFrame({
    "Date": ["2024-10-01", "2024-11-15", "2025-01-05"],
    "Hospital": ["Ottawa Central Hospital", "Ottawa General", "Ottawa Central Hospital"],
    "Department": ["Cardiology", "Endocrinology", "Psychiatry"],
    "Prescription Details": [
        "Amlodipine 5mg daily — Blood pressure control",
        "Metformin 500mg twice daily — Blood sugar control",
        "Sertraline 50mg daily — Anxiety management"
    ]
})

st.table(historical_prescriptions)

# ----------------------------
# 🤖 AI Health Assessment
# ----------------------------
st.subheader("🤖 AI Health Assessment")
st.write("""
Simulated AI Risk Scores:  
- **Heart Disease:** 6%  
- **Diabetes:** 12%  
- **Cancer:** Low  
""")

# ----------------------------
# 🩺 Footer
# ----------------------------
st.markdown("---")
st.caption("© 2025 Patient Portal | Streamlit Health Monitoring System")
