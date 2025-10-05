import streamlit as st
from PIL import Image, ImageSequence
import time

# --------------------------
# App Configuration
# --------------------------
st.set_page_config(
    page_title="NeuroScan",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS for dark theme
st.markdown("""
    <style>
        body {background-color: #0E1117; color: white;}
        .stApp {background-color: #0E1117;}
        h1, h2, h3, h4, h5 {color: #00FFAA;}
        .sidebar .sidebar-content {background-color: #1A1C23;}
        .stButton>button {background-color: #00FFAA; color: black; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# --------------------------
# Sidebar Navigation
# --------------------------
st.sidebar.title("🧭 Navigation")
st.sidebar.write("Select a page from below:")
st.sidebar.page_link("pages/1_Predict.py", label="🧠 Predict Tumor")
st.sidebar.page_link("pages/2_History.py", label="📜 Prediction History")
st.sidebar.page_link("pages/3_Login.py", label="🔐 Login / User Management")
st.sidebar.page_link("pages/4_About.py", label="ℹ️ About Project")

# --------------------------
# Main Page
# --------------------------
st.title("Welcome to 🧠 NeuroScan")
st.markdown("An AI-based multi-class brain tumor classification system built with **Deep Learning + Streamlit**.")

# Load and animate local GIF
gif_path = r"/home/rutanshu/Downloads/Deep-Learning---neuroscan(pd)/assets/Human_brain_MRI.gif"
img = Image.open(gif_path)

# Animate GIF frames
placeholder = st.empty()  # Placeholder to update the image
while True:
    for frame in ImageSequence.Iterator(img):
        placeholder.image(frame, use_container_width=True)
        time.sleep(0.1)
