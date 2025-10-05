import os
import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import time
from PIL import Image
from datetime import datetime

# App Configuration
# --------------------------
st.set_page_config(
    page_title="Predict Tumor",
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

    # --------------------------


# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(page_title="🧠 NeuroScan - Tumor Detection", layout="wide")

# --------------------------
# Load Model (cached)
# --------------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "brain_tumor_model.keras")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

CLASS_NAMES = ["No Tumor", "Tumor"]
IMG_SIZE = (150, 150)

# --------------------------
# Helper Functions
# --------------------------
def preprocess_image(image):
    """
    Resize and convert image to grayscale, normalize, and reshape for model.
    """
    img = image.resize(IMG_SIZE).convert("L")  # Grayscale
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=-1)  # channel dimension
    img_array = np.expand_dims(img_array, axis=0)   # batch dimension
    return img_array

def save_to_history(filename, result, confidence):
    """Save prediction result to history.csv"""
    history_path = os.path.join(os.path.dirname(__file__), "..", "history.csv")
    new_data = pd.DataFrame([{
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "filename": filename,
        "result": result,
        "confidence": f"{confidence:.2f}%"
    }])
    if os.path.exists(history_path):
        df = pd.read_csv(history_path)
        df = pd.concat([new_data, df], ignore_index=True)
    else:
        df = new_data
    df.to_csv(history_path, index=False)

# --------------------------
# Custom CSS
# --------------------------
st.markdown("""
    <style>
        .stApp {background-color: #0E1117; color: white;}
        .main-title {color: #00FFAA; font-size: 2.2em; font-weight: bold;}
        .prediction-box {
            background-color: #1E1E1E;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
        }
        .stButton>button {
            background-color: #00FFAA;
            color: black;
            border-radius: 10px;
            font-weight: bold;
        }
        .upload-box {
            background-color: #1A1C23;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------------
# UI Layout
# --------------------------
st.markdown('<h1 class="main-title">🧠 NeuroScan - Brain Tumor Detection</h1>', unsafe_allow_html=True)
st.write("Upload an MRI image to detect whether a tumor is present or not.")

uploaded_file = st.file_uploader("📤 Upload MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="🧩 Uploaded MRI Image", use_container_width=True)

    # Save uploaded image locally
    UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "uploaded_images")
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    image_save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    image.save(image_save_path)

    if st.button("🔍 Predict Tumor Presence"):
        with st.spinner("🔄 Analyzing MRI Image... Please wait..."):
            # Optional loading GIF
            gif_path = os.path.join(os.path.dirname(__file__), "..", "assets", "brain_loading.gif")
            if os.path.exists(gif_path):
                st.image(gif_path, width=180)

            # Progress bar animation
            progress_bar = st.progress(0)
            for percent in range(0, 101, 10):
                progress_bar.progress(percent)
                time.sleep(0.05)

            # --------------------------
            # Prediction
            # --------------------------
            processed_img = preprocess_image(image)
            prediction_prob = model.predict(processed_img, verbose=0)[0][0]

            # Binary classification
            if prediction_prob > 0.5:
                predicted_class = "Tumor"
                confidence = prediction_prob * 100
            else:
                predicted_class = "No Tumor"
                confidence = (1 - prediction_prob) * 100

        # Display prediction
        st.markdown(
            f"""
            <div class='prediction-box'>
                <h2>🧠 Prediction: <span style='color:#00FFAA'>{predicted_class}</span></h2>
                <h4>Confidence: {confidence:.2f}%</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Save to history
        save_to_history(uploaded_file.name, predicted_class, confidence)

else:
    st.info("👆 Please upload an MRI image to start prediction.")
