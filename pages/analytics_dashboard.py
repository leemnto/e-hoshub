import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# ----------------------------
# 🧭 Page Config
# ----------------------------
st.set_page_config(
    page_title="📊 Analytics & Management Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# 🏥 Sidebar
# ----------------------------
st.sidebar.header("🏥 Entity Selector")
entities = ["Hospital A", "Hospital B", "Hospital C"]
selected_entity = st.sidebar.selectbox("Select Hospital / Entity", entities)

st.sidebar.markdown("---")
st.sidebar.caption("📅 Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
st.sidebar.caption("⚙️ Streamlit Dashboard v2.0")

# ----------------------------
# 📦 Mock Data
# ----------------------------
entity_data = {
    "Hospital A": {
        "kpis": {"Diagnosis volume": 120, "Appointment volume": 320, "AI Accuracy": 87, "Patient retention": 74},
        "model": pd.DataFrame({
            "Disease": ["Heart", "Diabetes", "Cancer"],
            "Precision": [0.82, 0.76, 0.69],
            "Recall": [0.75, 0.68, 0.60],
            "F1": [0.78, 0.71, 0.64]
        })
    },
    "Hospital B": {
        "kpis": {"Diagnosis volume": 200, "Appointment volume": 500, "AI Accuracy": 91, "Patient retention": 80},
        "model": pd.DataFrame({
            "Disease": ["Heart", "Diabetes", "Cancer"],
            "Precision": [0.88, 0.79, 0.73],
            "Recall": [0.83, 0.72, 0.65],
            "F1": [0.85, 0.75, 0.69]
        })
    },
    "Hospital C": {
        "kpis": {"Diagnosis volume": 150, "Appointment volume": 400, "AI Accuracy": 85, "Patient retention": 70},
        "model": pd.DataFrame({
            "Disease": ["Heart", "Diabetes", "Cancer"],
            "Precision": [0.80, 0.70, 0.66],
            "Recall": [0.74, 0.65, 0.58],
            "F1": [0.77, 0.67, 0.61]
        })
    },
}

kpis = entity_data[selected_entity]["kpis"]
model_df = entity_data[selected_entity]["model"]

# ----------------------------
# 🎯 KPIs Section
# ----------------------------
st.markdown(f"## 📈 {selected_entity} — Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Diagnosis Volume", kpis["Diagnosis volume"])
col2.metric("Appointment Volume", kpis["Appointment volume"])
col3.metric("AI Accuracy", f"{kpis['AI Accuracy']}%")
col4.metric("Patient Retention", f"{kpis['Patient retention']}%")

# ----------------------------
# 📊 Model Performance Section
# ----------------------------
st.markdown("### 🤖 Model Performance Overview")

tab1, tab2 = st.tabs(["📋 Table View", "📊 Chart View"])

with tab1:
    st.dataframe(model_df, use_container_width=True)

with tab2:
    fig = px.bar(
        model_df,
        x="Disease",
        y=["Precision", "Recall", "F1"],
        barmode="group",
        color_discrete_sequence=px.colors.qualitative.Set2,
        title=f"Model Metrics by Disease ({selected_entity})"
    )
    fig.update_layout(height=400, template="plotly_white", showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# 📈 KPI Trends (last 30 days)
# ----------------------------
st.markdown("### 📆 KPI Trends (Past 30 Days)")

days = [datetime.now() - timedelta(days=i) for i in range(30)]
trend_df = pd.DataFrame({
    "Date": days[::-1],
    "Diagnosis volume": [kpis["Diagnosis volume"] + random.randint(-10, 10) for _ in range(30)],
    "Appointment volume": [kpis["Appointment volume"] + random.randint(-15, 15) for _ in range(30)],
    "AI Accuracy": [kpis["AI Accuracy"] + random.uniform(-2, 2) for _ in range(30)],
    "Patient retention": [kpis["Patient retention"] + random.uniform(-3, 3) for _ in range(30)],
})

metric_to_plot = st.selectbox("📊 Select Metric to View Trend", list(kpis.keys()), index=0)

trend_fig = px.line(
    trend_df,
    x="Date",
    y=metric_to_plot,
    title=f"{metric_to_plot} Trend Over Time",
    markers=True,
)
trend_fig.update_traces(line_color="#636EFA", line_width=3)
trend_fig.update_layout(height=400, template="plotly_white")
st.plotly_chart(trend_fig, use_container_width=True)

# ----------------------------
# ⚡ Radar Chart (Bonus Visualization)
# ----------------------------
st.markdown("### 🕹️ Model Metric Radar")

radar_fig = go.Figure()

radar_fig.add_trace(go.Scatterpolar(
    r=model_df["Precision"],
    theta=model_df["Disease"],
    fill='toself',
    name='Precision'
))
radar_fig.add_trace(go.Scatterpolar(
    r=model_df["Recall"],
    theta=model_df["Disease"],
    fill='toself',
    name='Recall'
))
radar_fig.add_trace(go.Scatterpolar(
    r=model_df["F1"],
    theta=model_df["Disease"],
    fill='toself',
    name='F1 Score'
))

radar_fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
    showlegend=True,
    template="plotly_dark",
    height=500
)
st.plotly_chart(radar_fig, use_container_width=True)

# ----------------------------
# 🧾 Footer
# ----------------------------
st.markdown("---")
st.caption("© 2025 HealthAI Analytics Dashboard | Built with ❤️ using Streamlit & Plotly")
