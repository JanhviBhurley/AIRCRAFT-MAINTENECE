import streamlit as st
from PIL import Image
import base64

# ===================== PAGE CONFIG =====================
st.set_page_config(page_title="Aircraft Maintenance App", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "home"

# Load background image
def get_base64_of_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

background_image_path = r"C:\Users\janhv\Desktop\project\Ame Project\data\UI.jpeg"
bg_image_base64 = get_base64_of_image(background_image_path)

# ===================== BACKGROUND =====================
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .content-box {{
        background-color: rgba(0, 0, 0, 0.5);
        padding: 20px;
        border-radius: 15px;
    }}
    .btn-style {{
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# ===================== PAGE TITLE =====================
st.markdown("<h1 style='text-align: center; color: white;'>✈️ Aircraft Maintenance Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: white;'>Smart Maintenance Real Time Analytics And AI Insights</h5>", unsafe_allow_html=True)

# ===================== TWO COLUMNS =====================
col1, col2 = st.columns([1, 1])  # left empty, right for content

with col1:
    st.empty()  # Leave left column empty

with col2:
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.markdown("""
        <h2 style='color:white;'> HEY AME's</h2>
        <p style='color:white; font-size:16px;'>
        "Safe skies begin with trusted care on the ground.
Our aircraft maintenance system ensures every journey is smooth, reliable, and worry-free.
With every check and every detail, we keep safety first and smiles flying high.
Because when maintenance is strong, confidence takes off!" ✈️✨
        </p>
        <h3 style='color:white;'> Let's Fly High! </h3>
        <ul style='color:white; font-size:16px;'>
            <li>Real-time AI-based aircraft health monitoring</li>
            <li>Alerts for upcoming component maintenance</li>
            <li>Historical maintenance tracking</li>
            <li>Predictive analytics for safe and efficient operations</li>
        </ul>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ===================== BUTTON TO NEXT PAGE =====================
    st.markdown('<div class="btn-style">', unsafe_allow_html=True)
    if st.button("Go to Aircrafts"):
        st.session_state.page = "aircraft_selection"
        st.switch_page("pages/aircraft_selection.py")
    st.markdown('</div>', unsafe_allow_html=True)
