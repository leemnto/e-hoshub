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
# 🩺 Simulated Patient Data
# ----------------------------
@st.cache_data
def generate_patient_data(seed):
    np.random.seed(seed)
    dates = pd.date_range(end=datetime.today(), periods=30)
    df = pd.DataFrame({
        "date": dates,
        "Temperature": 36.5 + np.random.randn(30) * 0.3,
        "Blood Pressure": 120 + np.random.randn(30),
        "Heart Rate": 70 + np.random.randn(30) * 2,
        "Weight": 65 + np.random.randn(30),
        "Height": 170 + np.random.randn(30) * 0.1
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
# 📊 Historical Trends (Bar Chart)
# ----------------------------
st.subheader("📊 Historical Trends (Weight & Height)")

trend_df = df.melt(
    id_vars="date",
    value_vars=["Weight", "Height"],
    var_name="Metric",
    value_name="Value"
)

fig = px.bar(
    trend_df,
    x="date",
    y="Value",
    color="Metric",
    barmode="group",
    title=f"Historical Trends — {selected_patient}",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig.update_layout(height=400, template="plotly_white", xaxis_title="Date", yaxis_title="Value")
st.plotly_chart(fig, use_container_width=True)

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
