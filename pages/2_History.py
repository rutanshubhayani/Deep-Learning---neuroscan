import os
from pathlib import Path
import pandas as pd
import streamlit as st
from itertools import islice

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
# Session / Access Control
# --------------------------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("🔐 Please log in to view prediction history.")
    st.stop()

# Only doctors or admins can view history
if st.session_state.get("role") not in {"Doctor", "Admin"}:
    st.error("⛔ Access denied. Only Doctors or Admins can view reports.")
    st.stop()

# --------------------------
# File Paths
# --------------------------
ROOT = Path(__file__).resolve().parent.parent  # project root (one level up)
HISTORY_PATH = ROOT / "history.csv"
UPLOAD_DIR = ROOT / "uploaded_images"

# --------------------------
# Custom CSS (dark polish)
# --------------------------
st.markdown(
    """
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
    """,
    unsafe_allow_html=True,
)

# --------------------------
# Title
# --------------------------
st.markdown('<h1 class="main-title">📜 Prediction History</h1>', unsafe_allow_html=True)
st.write("All your past MRI predictions are saved here.")

# --------------------------
# Load History Data
# --------------------------
if not HISTORY_PATH.exists() or HISTORY_PATH.stat().st_size == 0:
    st.info("No prediction history found yet. Upload and predict an MRI image first.")
    st.stop()

# Safer CSV read (handles BOM, etc.)
df = pd.read_csv(HISTORY_PATH)

# Normalize expected columns if needed
# (e.g., ensure there is a 'datetime' and 'filename' column)
if "datetime" in df.columns:
    # Sort by date (newest first)
    df = df.sort_values(by="datetime", ascending=False)

# --------------------------
# Display Table + Quick Filters
# --------------------------
with st.expander("🔎 View / Filter History", expanded=True):
    # Optional quick filter by patient / filename if columns exist
    left, right = st.columns(2)
    if "patient_id" in df.columns:
        pid = left.text_input("Filter by Patient ID (contains)")
        if pid:
            df = df[df["patient_id"].astype(str).str.contains(pid, case=False, na=False)]
    if "filename" in df.columns:
        fname = right.text_input("Filter by Filename (contains)")
        if fname:
            df = df[df["filename"].astype(str).str.contains(fname, case=False, na=False)]

    st.dataframe(df, use_container_width=True, hide_index=True)

# --------------------------
# Manage History
# --------------------------
with st.expander("⚙️ Manage History"):
    if st.button("🗑️ Clear All History"):
        try:
            HISTORY_PATH.unlink(missing_ok=True)
            st.success("History cleared successfully! Please refresh the page.")
        except Exception as e:
            st.error(f"Failed to clear history: {e}")

# --------------------------
# Thumbnails Grid
# --------------------------
st.markdown("### 🖼️ Image Thumbnails")

def chunked(iterable, n):
    it = iter(iterable)
    while True:
        chunk = list(islice(it, n))
        if not chunk:
            break
        yield chunk

cols_per_row = st.slider("Columns per row", min_value=3, max_value=8, value=5, step=1, help="Adjust how many thumbnails per row.")

if not UPLOAD_DIR.exists():
    st.info("No saved image thumbnails directory found.")
else:
    # Build list of unique existing image paths in df order
    file_list = []
    seen = set()
    if "filename" not in df.columns:
        st.info("No 'filename' column found in history to render thumbnails.")
    else:
        for fn in df["filename"]:
            if pd.isna(fn):
                continue
            fn = str(fn)
            if fn in seen:
                continue
            seen.add(fn)
            p = UPLOAD_DIR / fn
            if p.exists():
                file_list.append((fn, p))

        if not file_list:
            st.info("No saved image thumbnails found.")
        else:
            for row in chunked(file_list, cols_per_row):
                cols = st.columns(len(row), vertical_alignment="top")
                for (fn, p), col in zip(row, cols):
                    # use_container_width makes images responsive within their column
                    col.image(str(p), caption=fn, use_container_width=True)
