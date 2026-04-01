import streamlit as st
from components import home, disease, weather, voice, market

st.set_page_config(page_title="FarmIQ", layout="wide")

# -------- SESSION STATE --------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "lang" not in st.session_state:
    st.session_state.lang = "English"


# -------- NAVBAR --------
st.markdown("### 🌾 FarmIQ Navigation")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "home"

with col2:
    if st.button("📸 Disease Detection"):
        st.session_state.page = "disease"

with col3:
    if st.button("🌦 Weather + Alerts"):
        st.session_state.page = "weather"

with col4:
    if st.button("🎤 Voice Advisor"):
        st.session_state.page = "voice"

with col5:
    if st.button("💰 Market Intelligence"):
        st.session_state.page = "market"


# -------- PAGE ROUTING --------
pages = {
    "home": home,
    "disease": disease,
    "weather": weather,
    "voice": voice,
    "market": market
}

pages[st.session_state.page].show()


# -------- FOOTER --------
st.markdown("""
<hr>
<center>
🌾 FarmIQ - Smart Farming Assistant <br>
<small>© Source Code: Claude AI</small>
</center>
""", unsafe_allow_html=True)