import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px

# ----------------------------
# ⚙️ Page Config
# ----------------------------
st.set_page_config(page_title="Doctor Dashboard", layout="wide")

st.title("👩‍⚕️ Doctor Dashboard")
st.caption("For doctors to view patient AI diagnostics and clinical recommendations")

# ----------------------------
# 🧍‍♀️ Patient Selector
# ----------------------------
patients = ["Mary Poppings", "Jackson Wang"]
selected_patient = st.selectbox("Select Patient", patients)

# ----------------------------
# 🩺 Simulated Patient Data (Improved realism)
# ----------------------------
@st.cache_data
def generate_patient_data(seed):
    np.random.seed(seed)
    dates = pd.date_range(end=datetime.today(), periods=30)

    def smooth_series(base, noise_scale, smooth_window=5):
        noise = np.random.normal(0, noise_scale, len(dates))
        series = base + noise
        return pd.Series(series).rolling(window=smooth_window, min_periods=1, center=True).mean().values

    # General vitals (smooth fluctuations)
    temperature = smooth_series(36.6, 0.2)
    blood_pressure = smooth_series(120, 4)
    heart_rate = smooth_series(72, 2)

    df = pd.DataFrame({
        "date": dates,
        "Temperature": temperature,
        "Blood Pressure": blood_pressure,
        "Heart Rate": heart_rate
    })
    return df

if selected_patient == "Mary Poppings":
    df = generate_patient_data(42)
else:
    df = generate_patient_data(7)

# ----------------------------
# 📈 Vital Signs Chart
# ----------------------------
st.subheader("📉 Vital Signs Over Time (Temperature, Blood Pressure, Heart Rate)")
st.line_chart(
    df.set_index("date")[["Temperature", "Blood Pressure", "Heart Rate"]],
    use_container_width=True
)

# ----------------------------
# 🧬 AI Diagnostic Results
# ----------------------------
st.subheader("🧬 AI Diagnostic Results (Simulated)")
col1, col2, col3 = st.columns(3)

if selected_patient == "Mary Poppings":
    col1.metric("Heart Disease Risk", "6%")
    col2.metric("Diabetes Risk", "12%")
    col3.metric("Cancer Alert", "Low")
else:
    col1.metric("Heart Disease Risk", "15%")
    col2.metric("Diabetes Risk", "8%")
    col3.metric("Cancer Alert", "Medium")

# ----------------------------
# 💊 Current Prescriptions
# ----------------------------
st.subheader("💊 Current Prescriptions")

if selected_patient == "Mary Poppings":
    prescriptions = pd.DataFrame({
        "Medication": ["Amlodipine", "Metformin"],
        "Dosage": ["5 mg", "500 mg"],
        "Frequency": ["Once daily", "Twice daily"],
        "Purpose": ["Blood pressure control", "Blood sugar control"]
    })
else:
    prescriptions = pd.DataFrame({
        "Medication": ["Atorvastatin", "Losartan"],
        "Dosage": ["10 mg", "50 mg"],
        "Frequency": ["Once daily", "Once daily"],
        "Purpose": ["Cholesterol management", "Hypertension"]
    })

st.dataframe(prescriptions, use_container_width=True)

# ----------------------------
# 🧠 LLM Clinical Recommendation
# ----------------------------
st.subheader("🧠 LLM Clinical Recommendation")
st.write("This area will call an LLM API to generate a preliminary report based on AI diagnostics and recent trends.")

# ----------------------------
# 🩺 Footer
# ----------------------------
st.markdown("---")
st.caption(f"© 2025 Doctor Dashboard | Patient: {selected_patient} | Streamlit Health Monitoring System")
