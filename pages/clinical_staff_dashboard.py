import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# ----------------------------
# ⚙️ Page Config
# ----------------------------
st.set_page_config(page_title="Clinical Staff Dashboard", layout="wide")

st.title("👨‍⚕️ Clinical Staff Dashboard")
st.caption("For nurses and technicians to monitor patient status and tasks")

# ----------------------------
# 🏥 Mock Data
# ----------------------------
departments = {
    "Emergency / ER": {
        "Yue Liang": {
            "Test Results": pd.DataFrame({
                "Test ID": [101, 102],
                "Test Name": ["ECG", "Blood Pressure"],
                "Result": ["Normal", "High"],
                "Status": ["Completed", "Flagged"]
            }),
            "Upcoming Appointments": pd.DataFrame({
                "Date": [datetime.now() + timedelta(days=3)],
                "Purpose": ["Follow-up Consultation"],
                "Doctor": ["Dr. Smith"]
            }),
            "Follow-up Dates": pd.DataFrame({
                "Next Follow-up": [datetime.now() + timedelta(days=14)],
                "Notes": ["Monitor blood pressure daily"]
            }),
            "History Details": pd.DataFrame({
                "Date": [datetime.now() - timedelta(days=10), datetime.now() - timedelta(days=30)],
                "Event": ["Initial diagnosis", "Routine check-up"],
                "Outcome": ["Hypertension detected", "Normal"]
            })
        },
        "Jackson Wang": {
            "Test Results": pd.DataFrame({
                "Test ID": [103, 104],
                "Test Name": ["ECG", "Blood Test"],
                "Result": ["Irregular", "Normal"],
                "Status": ["Flagged", "Completed"]
            }),
            "Upcoming Appointments": pd.DataFrame({
                "Date": [datetime.now() + timedelta(days=5)],
                "Purpose": ["Cardiac monitoring"],
                "Doctor": ["Dr. Lee"]
            }),
            "Follow-up Dates": pd.DataFrame({
                "Next Follow-up": [datetime.now() + timedelta(days=20)],
                "Notes": ["Schedule stress test"]
            }),
            "History Details": pd.DataFrame({
                "Date": [datetime.now() - timedelta(days=15)],
                "Event": ["Chest pain report"],
                "Outcome": ["Observation ongoing"]
            })
        }
    },
    "Dental": {
        "Mary Poppings": {
            "Test Results": pd.DataFrame({
                "Test ID": [201],
                "Test Name": ["CT Scan"],
                "Result": ["Stable lesion"],
                "Status": ["Completed"]
            }),
            "Upcoming Appointments": pd.DataFrame({
                "Date": [datetime.now() + timedelta(days=7)],
                "Purpose": ["Treatment review"],
                "Doctor": ["Dr. Carter"]
            }),
            "Follow-up Dates": pd.DataFrame({
                "Next Follow-up": [datetime.now() + timedelta(days=30)],
                "Notes": ["Continue medication"]
            }),
            "History Details": pd.DataFrame({
                "Date": [datetime.now() - timedelta(days=40)],
                "Event": ["Cycle 1 Chemotherapy"],
                "Outcome": ["Tolerated well"]
            })
        }
    }
}

# ----------------------------
# 🔽 Filters
# ----------------------------
st.sidebar.header("🔍 Filters")

selected_dept = st.sidebar.selectbox("Select Department", list(departments.keys()))
patients = list(departments[selected_dept].keys())
selected_patient = st.sidebar.selectbox("Select Patient", patients)

patient_data = departments[selected_dept][selected_patient]

# ----------------------------
# 📦 Display Sections
# ----------------------------
st.markdown(f"### 🏥 Department: {selected_dept}")
st.markdown(f"### 👤 Patient: {selected_patient}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧪 Test Results")
    st.dataframe(patient_data["Test Results"], use_container_width=True)

with col2:
    st.subheader("📅 Upcoming Appointments")
    st.dataframe(patient_data["Upcoming Appointments"], use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("📆 Follow-up Dates")
    st.dataframe(patient_data["Follow-up Dates"], use_container_width=True)

with col4:
    st.subheader("📜 History Details")
    st.dataframe(patient_data["History Details"], use_container_width=True)

# ----------------------------
# 🔔 Alerts Section
# ----------------------------
st.markdown("### 🔔 Alerts")
if selected_patient == "Lisa Brown":
    st.warning("⚠️ Patient Lisa: Heart rate abnormal — nurse alerted.")
elif selected_patient == "John Doe":
    st.info("🩺 Patient John: Blood pressure above normal range.")
else:
    st.success("✅ No critical alerts for this patient.")

# ----------------------------
# 📄 Footer
# ----------------------------
st.markdown("---")
st.caption("© 2025 Clinical Staff Dashboard | Streamlit Health Monitoring System")
