import streamlit as st

st.set_page_config(page_title="E-Hospital Dashboard", layout="wide")

st.title("🏥 E-Hospital Interactive Dashboard")
st.write("Welcome to the E-hospital data management platform. Use the sidebar to switch roles.")

# 侧边栏导航
page = st.sidebar.radio(
    "Select a dashboard:",
    [
        "🏠 Home",
        "👩‍⚕️ Doctor Dashboard",
        "🧑 Patient Portal",
        "👨‍⚕️ Clinical Staff",
        "📊 Analytics & Management",
    ]
)

if page == "🏠 Home":
    st.header("System Overview")
    st.write("""
        This is a dashboard for an e-Hospital platform with four user roles:
        - Doctors
        - Patients
        - Clinical staff
        - Analysts / Management
    """)

elif page == "👩‍⚕️ Doctor Dashboard":
    st.experimental_set_query_params(page="doctor")
    st.write("Use the left sidebar to open the Doctor page, or go to /?page=doctor for direct link. (Streamlit pages folder also supported.)")
    # For multi-page apps, Streamlit auto-discovers pages in a `pages/` folder.
elif page == "🧑 Patient Portal":
    st.experimental_set_query_params(page="patient")
    st.write("Open the Patient Portal page.")
elif page == "👨‍⚕️ Clinical Staff":
    st.experimental_set_query_params(page="clinical")
    st.write("Open the Clinical Staff page.")
elif page == "📊 Analytics & Management":
    st.experimental_set_query_params(page="analytics")
    st.write("Open the Analytics & Management page.")
