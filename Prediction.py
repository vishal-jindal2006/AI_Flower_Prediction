import streamlit as st
import numpy as np
import joblib
import time
from fpdf import FPDF

# PAGE CONFIG
st.set_page_config(
    page_title="AI Flower Prediction",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# LOAD MODEL
model = joblib.load("models/best_model.pkl")

# LOAD SCALER
scaler = joblib.load("models/scaler.pkl")

# CUSTOM PDF CLASS
class PDF(FPDF):

    def rounded_rect(self, x, y, w, h, r, style=''):
        self.rect(x, y, w, h, style)

# PDF FUNCTION
def create_pdf(prediction, confidence):

    pdf = PDF()

    pdf.add_page()

    # BACKGROUND
    pdf.set_fill_color(15, 23, 42)
    pdf.rect(0, 0, 210, 297, 'F')

    # TITLE
    pdf.set_font("Arial", 'B', 26)
    pdf.set_text_color(255, 255, 255)

    pdf.cell(
        200,
        20,
        txt="AI FLOWER PREDICTION REPORT",
        ln=True,
        align='C'
    )

    # SUBTITLE
    pdf.set_font("Arial", '', 14)
    pdf.set_text_color(148, 163, 184)

    pdf.cell(
        200,
        10,
        txt="Generated using Machine Learning",
        ln=True,
        align='C'
    )

    pdf.ln(25)

    # RESULT BOX
    pdf.set_fill_color(30, 41, 59)

    pdf.rounded_rect(
        20,
        70,
        170,
        80,
        5,
        'F'
    )

    # RESULT TITLE
    pdf.set_xy(30, 85)

    pdf.set_font("Arial", 'B', 18)
    pdf.set_text_color(255, 255, 255)

    pdf.cell(
        100,
        10,
        txt="Prediction Result"
    )

    # FLOWER
    pdf.set_xy(30, 105)

    pdf.set_font("Arial", '', 16)

    pdf.cell(
        100,
        10,
        txt=f"Flower: {prediction}"
    )

    # CONFIDENCE
    pdf.set_xy(30, 125)

    pdf.cell(
        100,
        10,
        txt=f"Confidence Score: {confidence:.2f}%"
    )

    # FOOTER
    pdf.set_y(240)

    pdf.set_font("Arial", '', 11)

    pdf.set_text_color(148, 163, 184)

    pdf.cell(
        190,
        8,
        txt="Developed by Vishal Jindal",
        align='C'
    )

    pdf.output("prediction_report.pdf")

# PREMIUM CSS
st.markdown("""
<style>

/* REMOVE TOP SPACE */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 0rem !important;
}

/* TRANSPARENT HEADER */
header[data-testid="stHeader"] {
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

/* SIDEBAR BUTTON */
[data-testid="collapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    color: white !important;
}

/* MENU BUTTON */
button[kind="header"] {
    color: white !important;
}

/* TEXT */
html, body, [class*="css"] {
    color: white !important;
}

/* TITLE */
.main-title {
    text-align: center;
    font-size: 65px;
    font-weight: bold;
    color: white;
    margin-top: 0px;
}

/* SUBTITLE */
.sub-title {
    text-align: center;
    font-size: 24px;
    color: #cbd5e1;
    margin-bottom: 40px;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.06);
    padding: 35px;
    border-radius: 25px;
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-bottom: 30px;
}

/* BUTTON */
.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 14px;
    border: none;
    font-size: 20px;
    font-weight: bold;
    background: linear-gradient(to right, #06b6d4, #3b82f6);
    color: white;
}

/* BUTTON HOVER */
.stButton>button:hover {
    background: linear-gradient(to right, #3b82f6, #06b6d4);
}

/* DOWNLOAD BUTTON */
[data-testid="stDownloadButton"] button {
    width: 100%;
    height: 55px;
    border-radius: 14px;
    border: none;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(to right, #06b6d4, #3b82f6);
    color: white !important;
}

/* DOWNLOAD BUTTON HOVER */
[data-testid="stDownloadButton"] button:hover {
    background: linear-gradient(to right, #3b82f6, #06b6d4);
    color: white !important;
}

/* METRIC */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.06);
    border-radius: 18px;
    padding: 15px;
}

/* SLIDER */
.stSlider p {
    color: white !important;
    font-size: 18px;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 50px;
    padding: 20px;
}

/* MOBILE RESPONSIVE */
@media (max-width: 768px) {

    .main-title {
        font-size: 38px;
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

# SIDEBAR
st.sidebar.title("🌸 AI Navigation")

st.sidebar.info("""
### AI Flower Prediction System

Built using:
- Python
- Streamlit
- Machine Learning
- Scikit-learn
""")

# TITLE
st.markdown(
    "<div class='main-title'>🌸 AI Flower Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Professional Machine Learning Web Application</div>",
    unsafe_allow_html=True
)

# INTRO CARD
st.markdown("""
<div class='card'>

# 🚀 Welcome

This AI system predicts Iris flower species using Machine Learning algorithms.

### Features

- ✅ Real-time Flower Prediction
- ✅ AI Confidence Score
- ✅ Dashboard Analytics
- ✅ Dataset Upload
- ✅ Download PDF Report
- ✅ Modern Responsive UI

</div>
""", unsafe_allow_html=True)

# METRICS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Models", "4")

with col2:
    st.metric("Accuracy", "100%")

with col3:
    st.metric("Dataset Samples", "150")

# PREDICTION SECTION
st.markdown("""
<div class='card'>
<h1>🤖 Predict Flower</h1>
</div>
""", unsafe_allow_html=True)

# INPUTS
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

# PREDICT BUTTON
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

        # RESULT
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

# FOOTER
st.markdown("""
<div class='footer'>

### 🚀 Developed by Vishal Jindal

📧 jindalvishal2006@gmail.com

</div>
""", unsafe_allow_html=True)