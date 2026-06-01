import streamlit as st
import pandas as pd

# PAGE CONFIG
st.set_page_config(
    page_title="Upload Dataset",
    page_icon="📁",
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

/* REMOVE HEADER */
header[data-testid="stHeader"] {
    height: 0rem;
    background: transparent;
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

/* TEXT */
html, body, [class*="css"] {
    color: white !important;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.06);
    padding: 30px;
    border-radius: 22px;
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
}

/* DATAFRAME CONTAINER */
[data-testid="stDataFrame"] {
    background: rgba(15, 23, 42, 0.95) !important;
    border-radius: 18px;
    padding: 12px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* TABLE */
table {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 15px !important;
    overflow: hidden;
}

/* TABLE HEADER */
thead tr th {
    background-color: #1e293b !important;
    color: white !important;
    font-size: 16px !important;
}

/* TABLE ROWS */
tbody tr {
    background-color: #111827 !important;
    color: white !important;
}

/* TABLE HOVER */
tbody tr:hover {
    background-color: #1e293b !important;
}

/* TABLE BORDER */
td, th {
    border-color: rgba(255,255,255,0.08) !important;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.title("📁 Upload Dataset")

# CARD
st.markdown("<div class='card'>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ Dataset Uploaded Successfully!")

    st.subheader("Dataset Preview")

    st.dataframe(df.describe())

    st.subheader("Dataset Statistics")

    st.dataframe(df.describe())

st.markdown("</div>", unsafe_allow_html=True)