import streamlit as st
import pandas as pd

def show():

    st.markdown("<h2>📊 Market Intelligence</h2>", unsafe_allow_html=True)

    # Sample market data (you can later replace with real API)
    data = {
        "Crop": ["Rice", "Wheat", "Tomato", "Potato"],
        "Price (₹/kg)": [40, 30, 25, 20],
        "Best Season": ["Kharif", "Rabi", "Summer", "Winter"]
    }

    df = pd.DataFrame(data)

    st.dataframe(df)

    st.markdown("### 💡 Smart Suggestions")

    highest = df.loc[df["Price (₹/kg)"].idxmax()]

    st.success(f"💰 Highest Price Crop: {highest['Crop']} (₹{highest['Price (₹/kg)']}/kg)")

    st.info(f"🌱 Best to grow {highest['Crop']} in {highest['Best Season']} season for maximum profit.")