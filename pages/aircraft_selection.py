import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="Select Aircraft", layout="wide")

# ===================== BACKGROUND IMAGE =====================
def get_base64_of_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to your background image
background_image_path = "data/selection.jpeg"   # change path if needed
bg_image_base64 = get_base64_of_image(background_image_path)

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .brand-box img {{
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        transition: transform 0.3s;
    }}
    .brand-box img:hover {{
        transform: scale(1.05);
    }}
    </style>
""", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Select Aircraft Brand</h1>", unsafe_allow_html=True)

# Load logos (make sure you have the images in 'data/' folder)
aircraft_brands = {
    "Boeing": "data/BOEINGA.png",
    "Airbus": "data/AIRBUSA.png",
    "Comac": "data/COMAC.png",
    "Cessna": "data/CESSNA.png",
    "Piper": "data/PIPER.png",
    "Cirrus": "data/CIRRUS.png",
    "Embraer": "data/EMBRAER.png",
    "Bombardier": "data/BOMBARDIER.png"
}

# Function to display a brand with a button
def display_brand(brand_name, logo_path):
    st.image(logo_path, width=200)
    if st.button(f"Select {brand_name}"):
        st.session_state.selected_brand = brand_name
        st.switch_page("pages/aircraft_list.py")

# Display brands in a grid
cols = st.columns(4)  # 4 brands per row
i = 0
for brand, logo in aircraft_brands.items():
    with cols[i % 4]:
        display_brand(brand, logo)
    i += 1
