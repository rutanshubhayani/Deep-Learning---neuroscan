import streamlit as st

# --------------------------
# App Configuration
# --------------------------
st.set_page_config(
    
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(page_title="ℹ️ About NeuroScan", layout="wide")

# --------------------------
# Custom CSS
# --------------------------
st.markdown("""
    <style>
        .stApp {background-color: #0E1117; color: white;}
        .main-title {color: #00FFAA; font-size: 2.3em; font-weight: bold; text-align:center;}
        .sub-title {color: #FFDD00; font-size: 1.4em; font-weight: 600; margin-top: 30px;}
        .info-box {
            background-color: #1E1E1E;
            padding: 20px;
            border-radius: 15px;
            margin-top: 15px;
        }
        .tech-badge {
            display: inline-block;
            background-color: #00FFAA;
            color: black;
            font-weight: bold;
            padding: 6px 12px;
            margin: 5px;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------------
# Title
# --------------------------
st.markdown('<h1 class="main-title">ℹ️ About NeuroScan</h1>', unsafe_allow_html=True)

# --------------------------
# Project Overview
# --------------------------
st.markdown("""
<div class="info-box">
    <p>
        <strong>NeuroScan 🧠</strong> is an advanced <strong>Deep Learning-based Brain Tumor Classification System</strong> 
        designed to assist doctors and technicians in detecting different types of brain tumors from MRI scans.
    </p>
   
</div>
""", unsafe_allow_html=True)

# --------------------------
# Features
# --------------------------
st.markdown('<h2 class="sub-title">🚀 Key Features</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-box">
        <ul>
            <li>📤 Upload MRI images for prediction</li>
            <li>🔍 Real-time tumor type classification</li>
            <li>📜 Prediction history logging</li>
            <li>🔐 Role-based login system</li>
            <li>🌗 Dark mode interface</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
        <ul>
            <li>📊 Confidence score visualization</li>
            <li>🧠 Animated prediction process</li>
            <li>👨‍⚕️ Doctor & Technician modes</li>
            <li>💾 Local data persistence</li>
            <li>🧩 Modular architecture for expansion</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --------------------------
# Tech Stack
# --------------------------
st.markdown('<h2 class="sub-title">🧰 Technology Stack</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    <span class="tech-badge">Python</span>
    <span class="tech-badge">TensorFlow / Keras</span>
    <span class="tech-badge">Streamlit</span>
    <span class="tech-badge">NumPy</span>
    <span class="tech-badge">Pandas</span>
    <span class="tech-badge">Pillow</span>
    <span class="tech-badge">Matplotlib</span>
</div>
""", unsafe_allow_html=True)

# --------------------------
# Vision Statement
# --------------------------
st.markdown('<h2 class="sub-title">🌍 Our Vision</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    <p>
        NeuroScan aims to bridge the gap between Artificial Intelligence and Medical Diagnostics,
        empowering healthcare professionals with rapid, reliable, and interpretable insights 
        from MRI scans — to enable faster decision-making and improved patient outcomes.
    </p>
</div>
""", unsafe_allow_html=True)
