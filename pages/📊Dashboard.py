import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# PAGE CONFIG
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# LOAD DATA
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["target"] = iris.target

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
    margin-bottom: 25px;
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

h1, h2, h3 {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.title("📊 AI Dashboard")

# DATA PREVIEW
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("Dataset Preview")

st.dataframe(df.describe())

st.markdown("</div>", unsafe_allow_html=True)

# STATISTICS
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("Statistics")

st.dataframe(df.describe())

st.markdown("</div>", unsafe_allow_html=True)

# HEATMAP
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(10,5))

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax
)

fig.patch.set_facecolor('#111827')

st.pyplot(fig)

st.markdown("</div>", unsafe_allow_html=True)