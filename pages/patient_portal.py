import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Patient Portal", layout="wide")

st.title("🧑 Patient Portal")
st.caption("For patients to view personal health trends and AI assessments")

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
st.line_chart(df.set_index("date")[["systolic_bp", "diastolic_bp", "heart_rate"]])

st.subheader("🤖 AI Health Assessment")
st.write("Simulated risk scores:\n- Heart disease: 6%\n- Diabetes: 12%\n- Cancer: Low")
