import os
import streamlit as st
import pandas as pd
from PIL import Image

# --------------------------
# App Configuration
# --------------------------
st.set_page_config(
    page_title="📜 Prediction History",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------
# Login Check
# --------------------------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("🔐 Please log in to view prediction history.")
    st.stop()

# Only doctors or admins can view history
if st.session_state.role not in ["Doctor", "Admin"]:
    st.error("⛔ Access denied. Only Doctors or Admins can view reports.")
    st.stop()



# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(page_title="📜 Prediction History", layout="wide")

# --------------------------
# File Paths
# --------------------------
HISTORY_PATH = os.path.join(os.path.dirname(__file__), "..", "history.csv")
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "uploaded_images")

# --------------------------
# Custom CSS
# --------------------------
st.markdown("""
    <style>
        .stApp {background-color: #0E1117; color: white;}
        .main-title {color: #00FFAA; font-size: 2em; font-weight: bold;}
        .history-table td, .history-table th {
            padding: 10px;
            border-bottom: 1px solid #333;
        }
        .stButton>button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 10px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------------
# Page Title
# --------------------------
st.markdown('<h1 class="main-title">📜 Prediction History</h1>', unsafe_allow_html=True)
st.write("All your past MRI predictions are saved here.")

# --------------------------
# Load History Data
# --------------------------
if not os.path.exists(HISTORY_PATH) or os.stat(HISTORY_PATH).st_size == 0:
    st.info("No prediction history found yet. Upload and predict an MRI image first.")
else:
    df = pd.read_csv(HISTORY_PATH)

    # Sort by date (newest first)
    df = df.sort_values(by="datetime", ascending=False)

    # --------------------------
    # Display Table
    # --------------------------
    st.dataframe(df, use_container_width=True, hide_index=True)

    # --------------------------
    # Option: Clear History
    # --------------------------
    with st.expander("⚙️ Manage History"):
        if st.button("🗑️ Clear All History"):
            os.remove(HISTORY_PATH)
            st.success("History cleared successfully! Please refresh the page.")

    # --------------------------
    # Optional: Display Thumbnails
    # --------------------------
    st.markdown("### 🖼️ Image Thumbnails (if available)")
    if os.path.exists(UPLOAD_DIR):
        for filename in df["filename"].unique():
            file_path = os.path.join(UPLOAD_DIR, filename)
            if os.path.exists(file_path):
                st.image(file_path, caption=filename, width=150)
    else:
        st.info("No saved image thumbnails found.")
