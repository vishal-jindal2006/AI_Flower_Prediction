import streamlit as st
import pandas as pd
import os

# PAGE CONFIG
st.set_page_config(
    page_title="Contact",
    page_icon="📞",
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
    padding: 35px;
    border-radius: 22px;
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* INPUT FIELDS */
.stTextInput input,
.stTextArea textarea {
    background: rgba(15, 23, 42, 0.95) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 14px !important;
    padding: 12px !important;
}

/* PLACEHOLDER */
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #94a3b8 !important;
}

/* LABELS */
label {
    color: white !important;
    font-weight: 500;
}

/* BUTTON */
.stButton>button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(to right, #06b6d4, #3b82f6);
    color: white;
    font-size: 18px;
    font-weight: bold;
}

/* BUTTON HOVER */
.stButton>button:hover {
    background: linear-gradient(to right, #3b82f6, #06b6d4);
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.title("📞 Contact Us")

# CARD
st.markdown("<div class='card'>", unsafe_allow_html=True)

# INPUTS
name = st.text_input(
    "Enter Your Name",
    placeholder="Vishal Jindal"
)

email = st.text_input(
    "Enter Your Email",
    placeholder="jindalvishal2006@gmail.com"
)

message = st.text_area(
    "Enter Message",
    placeholder="Write your message here..."
)

# BUTTON
if st.button("Send Message"):

    if name and email and message:

        # DATA
        new_data = pd.DataFrame({
            "Name": [name],
            "Email": [email],
            "Message": [message]
        })

        # FILE NAME
        file_name = "messages.csv"

        # SAVE CSV
        if os.path.exists(file_name):

            old_data = pd.read_csv(file_name)

            updated_data = pd.concat(
                [old_data, new_data],
                ignore_index=True
            )

            updated_data.to_csv(
                file_name,
                index=False
            )

        else:

            new_data.to_csv(
                file_name,
                index=False
            )

        st.success("✅ Message Saved Successfully!")

    else:

        st.error("❌ Please fill all fields.")

st.markdown("</div>", unsafe_allow_html=True)

# EMAIL INFO
st.info("""
📧 jindalvishal2006@gmail.com
""")