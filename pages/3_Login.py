import streamlit as st

# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(page_title="🔐 NeuroScan Login", layout="centered")

# --------------------------
# User Database (Temporary)
# --------------------------
USER_DB = {
    "doctor": {"password": "doc123", "role": "Doctor"},
    "tech": {"password": "tech123", "role": "Technician"},
    "admin": {"password": "admin123", "role": "Admin"},
}

# --------------------------
# Custom CSS
# --------------------------
st.markdown("""
    <style>
        .stApp {background-color: #0E1117; color: white;}
        .main-title {color: #00FFAA; font-size: 2em; font-weight: bold; text-align:center;}
        .login-box {
            background-color: #1E1E1E;
            padding: 30px;
            border-radius: 15px;
            width: 400px;
            margin: 0 auto;
        }
        .stButton>button {
            background-color: #00FFAA;
            color: black;
            border-radius: 10px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------------
# Initialize Session State
# --------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.role = None

# --------------------------
# Title
# --------------------------
st.markdown('<h1 class="main-title">🔐 NeuroScan Login</h1>', unsafe_allow_html=True)

# --------------------------
# Login Form
# --------------------------
if not st.session_state.logged_in:
    with st.container():
        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")

        if st.button("Login"):
            if username in USER_DB and USER_DB[username]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.role = USER_DB[username]["role"]
                st.success(f"✅ Logged in as {st.session_state.role}")
                st.info("➡️ Navigate to the appropriate page based on your role.")
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")
        st.markdown("</div>", unsafe_allow_html=True)

# --------------------------
# Logged-in View with Role-Based Features
# --------------------------
else:
    st.success(f"Welcome, {st.session_state.username}! 👋 Role: {st.session_state.role}")

    # Role-based access
    if st.session_state.role == "Doctor":
        st.info("🧠 You can view detailed reports and patient history. Prediction feature is not available.")
    elif st.session_state.role == "Technician":
        st.info("🧪 You can upload and scan MRI images for tumor prediction.")
        # Show prediction button (simulate link to prediction page)
        if st.button("➡️ Go to MRI Prediction Page"):
            st.experimental_set_query_params(page="prediction")
            st.info("Redirect to prediction page here (implement page navigation).")
    elif st.session_state.role == "Admin":
        st.info("🧑‍💼 You have full system access, including user management. Prediction feature is hidden.")

    # Logout button
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.role = None
        st.success("🔒 Logged out successfully!")
        st.rerun()
