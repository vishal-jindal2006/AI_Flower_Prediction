import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# PREMIUM CSS
st.markdown("""
<style>

/* REMOVE WHITE SPACE */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
}

/* REMOVE HEADER SPACE */
header[data-testid="stHeader"] {
    height: 0rem;
    background: rgba(0,0,0,0);
}

/* REMOVE TOOLBAR */
[data-testid="stToolbar"] {
    display: none;
}

/* REMOVE DECORATION */
[data-testid="stDecoration"] {
    display: none;
}

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(to right, #020617, #0f172a);
    color: white;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #020617, #111827);
}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.06);
    padding: 35px;
    border-radius: 22px;
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.title("ℹ️ About Project")

# CARD
st.markdown("""
<div class='card'>

# 🌸 AI Flower Prediction System

Professional Machine Learning Web Application.

## 🚀 Features

- Real-time Flower Prediction
- AI Confidence Score
- Dashboard Analytics
- Dataset Upload
- Modern Responsive UI

## 🤖 Algorithms Used

- KNN
- Random Forest
- SVM
- Logistic Regression

## 👨‍💻 Developer

Vishal Jindal

📧 jindalvishal2006@gmail.com

</div>
""", unsafe_allow_html=True)