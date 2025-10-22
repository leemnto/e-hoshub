# 🏥 E-Hospital Dashboard (Streamlit Prototype)

This is a Streamlit prototype for an interactive medical dashboard with four user roles:
- 👩‍⚕️ Doctor
- 🧑 Patient
- 👨‍⚕️ Clinical Staff
- 📊 Analyst / Management

## 🧰 Quick Start (Local)

```bash
python -m venv venv
source venv/bin/activate        # or venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run main.py
```

## ☁️ Deploy to Streamlit Cloud

1. Push this repo to GitHub.
2. Go to https://streamlit.io/cloud
3. New app → GitHub repo → Branch: main → File: main.py
4. Advanced settings: choose Python 3.10 or 3.11
5. Click Deploy ✅

Once deployed, your app will be live at: https://your-app-name.streamlit.app

**Tips:** pin numpy & pandas versions to avoid build errors.
