import streamlit as st
from utils.weather_api import get_weather
from utils.alerts import generate_alerts


def show():
    st.markdown("<h2>🌦 Weather Intelligence</h2>", unsafe_allow_html=True)

    city = st.text_input("Enter City", "Bangalore")

    if st.button("Get Weather"):
        data = get_weather(city)

        temp = data["temperature"]
        humidity = data["humidity"]
        condition = data["condition"]

        st.success(f"🌡 Temperature: {temp}°C")
        st.info(f"💧 Humidity: {humidity}%")
        st.write(f"☁ Condition: {condition}")

        alert = generate_alerts(humidity)
        st.warning(alert)
