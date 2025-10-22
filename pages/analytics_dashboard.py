import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analytics Dashboard", layout="wide")

st.title("📊 Analytics & Management Dashboard")
st.caption("For analysts to monitor KPIs and model performance")

kpis = {
    "Diagnosis volume": 120,
    "Appointment volume": 320,
    "AI Accuracy": "87%",
    "Patient retention": "74%"
}

col1, col2, col3, col4 = st.columns(4)
for i, (k, v) in enumerate(kpis.items()):
    [col1, col2, col3, col4][i].metric(k, v)

st.subheader("🤖 Model Performance")
st.table(pd.DataFrame({
    "Disease": ["Heart", "Diabetes", "Cancer"],
    "Precision": [0.82, 0.76, 0.69],
    "Recall": [0.75, 0.68, 0.60],
    "F1": [0.78, 0.71, 0.64]
}))
