import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load trained model
model = load_model("pneumonia_model-1.h5")

# App title
st.title("🩺 Pneumonia Detection from Chest X-ray")
st.write("Upload a chest X-ray image to detect if it shows signs of **Pneumonia** or is **Normal**.")

# Upload image
uploaded_file = st.file_uploader("Choose an X-ray image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded X-ray", use_column_width=True)

    # Preprocess
    img_resized = img.resize((150, 150))
    img_array = image.img_to_array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)[0][0]
    label = "Pneumonia" if prediction > 0.5 else "Normal"
    confidence = prediction if prediction > 0.5 else 1 - prediction

    st.markdown(f"### 🧠 Prediction: `{label}`")
    st.markdown(f"### 🔍 Confidence: `{confidence:.2%}`")
