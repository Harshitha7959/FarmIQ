import streamlit as st
from PIL import Image
import random

def show():

    st.markdown("<h2>📸 Disease Detection</h2>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload Crop Leaf Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:

        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("🔍 Detect Disease"):

            # -------- SMART RANDOM (REALISTIC) --------
            diseases = [
                ("Leaf Blight", "Apply fungicide spray immediately"),
                ("Powdery Mildew", "Use sulfur-based pesticide"),
                ("Rust Disease", "Use copper fungicide"),
                ("Leaf Spot", "Remove infected leaves and spray fungicide"),
                ("Healthy", "Crop is healthy, maintain current care")
            ]

            result = random.choice(diseases)

            # Confidence more realistic
            if result[0] == "Healthy":
                confidence = round(random.uniform(88, 98), 2)
            else:
                confidence = round(random.uniform(80, 95), 2)

            # -------- DISPLAY RESULT --------
            st.markdown("### 🧠 Prediction Result")

            st.success(f"🦠 Disease Detected: {result[0]}")
            st.info(f"📊 Confidence: {confidence}%")

            if result[0] == "Healthy":
                st.success("✅ Crop looks healthy.")
            else:
                st.warning(f"⚠️ Recommendation: {result[1]}")

            st.caption("ℹ️ This is AI-simulated prediction for prototype demonstration.")
