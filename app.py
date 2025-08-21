import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model("brain_tumor_model.keras") 

CLASS_NAMES = ["No Tumor", "Tumor"]

# Image preprocessing function
def preprocess_image(image):
    img = image.resize((150, 150))  # match model input size
    img_array = np.array(img) / 255.0  # normalize
    if len(img_array.shape) == 2:  # if grayscale
        img_array = np.expand_dims(img_array, axis=-1)  # add channel dimension
    img_array = np.expand_dims(img_array, axis=0)  # add batch dimension
    return img_array

# Streamlit UI
st.title("Brain Tumor Prediction")
uploaded_file = st.file_uploader("Choose an MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")  # convert to grayscale
    # Updated line to fix the deprecation warning
    st.image(image, caption="Uploaded MRI", use_container_width=True)

    if st.button("Predict"):
        processed_img = preprocess_image(image)
        prediction = model.predict(processed_img)[0][0]  # Get the single probability value
        
        # Determine the class based on a threshold (e.g., 0.5)
        if prediction > 0.5:
            predicted_class = CLASS_NAMES[1]
            confidence = prediction * 100
        else:
            predicted_class = CLASS_NAMES[0]
            confidence = (1 - prediction) * 100
        
        st.success(f"Prediction: **{predicted_class}** ({confidence:.2f}% confidence)")