import streamlit as st
from utils.weather_api import get_weather
from utils.alerts import generate_alerts

def show():

    st.markdown("<h2>🌦 Weather Intelligence</h2>", unsafe_allow_html=True)

    city = st.text_input("Enter City", "Bangalore")

    if st.button("Get Weather"):

 def get_weather(city):
    return {
        "temperature": 28,
        "humidity": 75,
        "condition": f"Cloudy in {city}"
    }

        # -------- DATA --------
        temp = data["temp"]
        humidity = data["humidity"]
        rain = data["rain"]

        # -------- DISPLAY WEATHER --------
        st.markdown(f"""
        <div class="card">
        🌡 Temperature: {temp}°C <br>
        💧 Humidity: {humidity}% <br>
        🌧 Rain Probability: {rain}%
        </div>
        """, unsafe_allow_html=True)

        # -------- ALERT ENGINE --------
        alerts = generate_alerts(temp, humidity, rain)

        st.markdown("### ⚠️ Smart Decision Alerts")

        for alert in alerts:

            if alert["type"] == "warning":
                st.warning(alert["message"])

            elif alert["type"] == "info":
                st.info(alert["message"])

            elif alert["type"] == "success":
                st.success(alert["message"])
