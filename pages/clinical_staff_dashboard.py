import streamlit as st
import pandas as pd

st.set_page_config(page_title="Clinical Staff", layout="wide")

st.title("👨‍⚕️ Clinical Staff Dashboard")
st.caption("For nurses and technicians to monitor patient status and tasks")

st.subheader("📦 Test and Report Status")
st.table(pd.DataFrame({
    "Test ID": [1001, 1002, 1003],
    "Patient": ["John", "Mary", "Lisa"],
    "Status": ["Processing", "Ready", "Processing"]
}))

st.subheader("🔔 Alerts")
st.warning("Patient Lisa: Heart rate abnormal — nurse alerted")
