import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Doctor Dashboard", layout="wide")

st.title("👩‍⚕️ Doctor Dashboard")
st.caption("For doctors to view patient AI diagnostics and clinical recommendations")

@st.cache_data
def patient_data():
    dates = pd.date_range(end=datetime.today(), periods=30)
    df = pd.DataFrame({
        "date": dates,
        "systolic_bp": 120 + np.random.randn(30).cumsum(),
        "diastolic_bp": 80 + np.random.randn(30).cumsum(),
        "heart_rate": 70 + np.random.randn(30) * 2
    })
    return df

df = patient_data()
st.line_chart(df.set_index("date")[["systolic_bp", "diastolic_bp", "heart_rate"]])

st.subheader("🧬 AI Diagnostic Results (Simulated)")
col1, col2, col3 = st.columns(3)
col1.metric("Heart Disease Risk", "6%")
col2.metric("Diabetes Risk", "12%")
col3.metric("Cancer Alert", "Low")

st.subheader("🧠 LLM Clinical Recommendation")
st.write("This area will call an LLM API to generate a preliminary report.")
