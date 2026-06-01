import streamlit as st
import numpy as np
import joblib
import time
from fpdf import FPDF

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Flower Prediction",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("models/best_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# ==========================================
# PDF CLASS
# ==========================================

class PDF(FPDF):

    def header(self):

        self.set_fill_color(15, 23, 42)

        self.rect(0, 0, 210, 297, 'F')

        self.set_font("Arial", "B", 24)

        self.set_text_color(255, 255, 255)

        self.ln(10)

        self.cell(
            190,
            10,
            "AI FLOWER PREDICTION REPORT",
            ln=True,
            align="C"
        )

        self.ln(5)

        self.set_font("Arial", "", 12)

        self.set_text_color(180, 180, 180)

        self.cell(
            190,
            10,
            "Generated using Machine Learning",
            ln=True,
            align="C"
        )

        self.ln(20)

    def footer(self):

        self.set_y(-20)

        self.set_font("Arial", "", 10)

        self.set_text_color(150, 150, 150)

        self.cell(
            0,
            10,
            "Developed by Vishal Jindal",
            align="C"
        )

# ==========================================
# CREATE PDF
# ==========================================

def create_pdf(prediction, confidence):

    pdf = PDF()

    pdf.add_page()

    # RESULT CARD
    pdf.set_fill_color(30, 41, 59)

    pdf.rect(
        25,
        80,
        160,
        70,
        'F'
    )

    # TITLE
    pdf.set_xy(35, 95)

    pdf.set_font("Arial", "B", 18)

    pdf.set_text_color(255, 255, 255)

    pdf.cell(
        100,
        10,
        "Prediction Result"
    )

    # FLOWER
    pdf.set_xy(35, 115)

    pdf.set_font("Arial", "", 15)

    pdf.cell(
        100,
        10,
        f"Flower: {prediction}"
    )

    # CONFIDENCE
    pdf.set_xy(35, 130)

    pdf.cell(
        100,
        10,
        f"Confidence Score: {confidence:.2f}%"
    )

    pdf.output("prediction_report.pdf")

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* ==========================================
   REMOVE STREAMLIT DEFAULTS
========================================== */

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 0rem !important;
}

header[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stDecoration"] {
    display: none;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ==========================================
   MAIN BACKGROUND
========================================== */

.stApp {
    background: linear-gradient(to right, #020617, #0f172a);
    color: white;
}

/* ==========================================
   SIDEBAR
========================================== */

section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #020617, #111827);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* ==========================================
   SIDEBAR MENU BUTTON
========================================== */

button[kind="header"] {

    background: rgba(255,255,255,0.08) !important;

    border-radius: 12px !important;

    width: 52px !important;
    height: 52px !important;

    border: none !important;

    backdrop-filter: blur(10px);

    transition: 0.3s;

    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

/* HOVER EFFECT */

button[kind="header"]:hover {

    background: rgba(255,255,255,0.15) !important;

    transform: scale(1.05);
}

/* MENU ICON */

button[kind="header"] svg {

    color: #d1d5db !important;

    width: 38px !important;
    height: 38px !important;
}

/* ==========================================
   TITLES
========================================== */

.main-title {

    text-align: center;

    font-size: 65px;

    font-weight: bold;

    color: white;
}

.sub-title {

    text-align: center;

    font-size: 24px;

    color: #cbd5e1;

    margin-bottom: 40px;
}

/* ==========================================
   GLASS CARD
========================================== */

.card {

    background: rgba(255,255,255,0.06);

    padding: 35px;

    border-radius: 25px;

    backdrop-filter: blur(14px);

    box-shadow: 0 8px 32px rgba(0,0,0,0.3);

    margin-bottom: 30px;
}

/* ==========================================
   BUTTONS
========================================== */

.stButton > button {

    width: 100%;

    height: 55px;

    border-radius: 14px;

    border: none;

    font-size: 20px;

    font-weight: bold;

    background: linear-gradient(
        to right,
        #06b6d4,
        #3b82f6
    );

    color: white;
}

.stButton > button:hover {

    background: linear-gradient(
        to right,
        #3b82f6,
        #06b6d4
    );
}

/* ==========================================
   DOWNLOAD BUTTON
========================================== */

[data-testid="stDownloadButton"] button {

    width: 100%;

    height: 55px;

    border-radius: 14px;

    border: none;

    font-size: 18px;

    font-weight: bold;

    background: linear-gradient(
        to right,
        #06b6d4,
        #3b82f6
    );

    color: white !important;
}

/* ==========================================
   METRICS
========================================== */

[data-testid="metric-container"] {

    background: rgba(255,255,255,0.06);

    border-radius: 18px;

    padding: 15px;
}

/* ==========================================
   SLIDER
========================================== */

.stSlider p {

    color: white !important;

    font-size: 18px;
}

/* ==========================================
   FOOTER
========================================== */

.footer {

    text-align: center;

    color: #94a3b8;

    margin-top: 50px;

    padding: 20px;
}

/* ==========================================
   MOBILE
========================================== */

@media (max-width: 768px) {

    .main-title {
        font-size: 42px;
    }

    .sub-title {
        font-size: 18px;
    }

    .card {
        padding: 20px;
    }
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🌸 AI Navigation")

st.sidebar.info("""
### AI Flower Prediction

Built using:
- Python
- Streamlit
- Machine Learning
- Scikit-learn
""")

# ==========================================
# TITLE
# ==========================================

st.markdown(
    "<div class='main-title'>🌸 AI Flower Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Professional Machine Learning Web Application</div>",
    unsafe_allow_html=True
)

# ==========================================
# WELCOME CARD
# ==========================================

st.markdown("""
<div class='card'>

# 🚀 Welcome

This AI system predicts Iris flower species using Machine Learning algorithms.

### Features

- ✅ Real-time Flower Prediction
- ✅ AI Confidence Score
- ✅ Download PDF Report
- ✅ Modern Responsive UI

</div>
""", unsafe_allow_html=True)

# ==========================================
# METRICS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Models", "4")

with col2:
    st.metric("Accuracy", "100%")

with col3:
    st.metric("Dataset Samples", "150")

# ==========================================
# PREDICTION SECTION
# ==========================================

st.markdown("""
<div class='card'>
<h1>🤖 Predict Flower</h1>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    sl = st.slider(
        "Sepal Length",
        4.0,
        8.0,
        5.1
    )

    sw = st.slider(
        "Sepal Width",
        2.0,
        5.0,
        3.5
    )

with col2:

    pl = st.slider(
        "Petal Length",
        1.0,
        7.0,
        1.4
    )

    pw = st.slider(
        "Petal Width",
        0.1,
        3.0,
        0.2
    )

# ==========================================
# PREDICT BUTTON
# ==========================================

if st.button("🚀 Predict Flower"):

    with st.spinner("Analyzing Flower Data..."):

        time.sleep(2)

        data = np.array([
            [sl, sw, pl, pw]
        ])

        scaled_data = scaler.transform(data)

        prediction = model.predict(scaled_data)

        probability = model.predict_proba(scaled_data)

        flowers = [
            "Setosa",
            "Versicolor",
            "Virginica"
        ]

        confidence = np.max(probability) * 100

        predicted_flower = flowers[prediction[0]]

        st.success(
            f"Prediction: {predicted_flower}"
        )

        st.info(
            f"Confidence Score: {confidence:.2f}%"
        )

        st.progress(int(confidence))

        # CREATE PDF
        create_pdf(
            predicted_flower,
            confidence
        )

        # DOWNLOAD BUTTON
        with open(
            "prediction_report.pdf",
            "rb"
        ) as pdf_file:

            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_file,
                file_name="prediction_report.pdf",
                mime="application/pdf"
            )

# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class='footer'>

### 🚀 Developed by Vishal Jindal

📧 jindalvishal2006@gmail.com

</div>
""", unsafe_allow_html=True)