import streamlit as st

def show():

    # -------- TITLE --------
    st.markdown("""
    <div style="
        text-align:center;
        font-size:48px;
        font-weight:bold;
        color:#22c55e;
        text-shadow: 
            0px 0px 5px rgba(34,197,94,0.9),
            0px 0px 15px rgba(34,197,94,0.7),
            0px 0px 30px rgba(34,197,94,0.5);
    ">
        🌾 FarmIQ
    </div>

    <div style="
        text-align:center;
        color:#94a3b8;
        font-size:18px;
        margin-bottom:30px;
    ">
        AI-powered Smart Farming Decision System
    </div>
    """, unsafe_allow_html=True)

    # -------- FEATURES --------
    st.markdown('<div class="section-title">🚀 Core Features</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # -------- LEFT COLUMN --------
    with col1:

        st.markdown("""
        <div class="card">
        <h3>📸 Disease Detection</h3>
        <p>Upload crop images and detect diseases using AI</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Go → Disease"):
            st.session_state.page = "disease"
            st.rerun()


        st.markdown("""
        <div class="card">
        <h3>🎤 Voice Advisor</h3>
        <p>Ask questions in English or Kannada and get voice responses</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Go → Voice"):
            st.session_state.page = "voice"
            st.rerun()


    # -------- RIGHT COLUMN --------
    with col2:

        st.markdown("""
        <div class="card">
        <h3>🌦 Weather + Smart Alerts</h3>
        <p>Get real-time weather insights with intelligent farming alerts</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Go → Weather"):
            st.session_state.page = "weather"
            st.rerun()


        st.markdown("""
        <div class="card">
        <h3>💰 Market Intelligence</h3>
        <p>Analyze crop prices and choose the most profitable crops</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Go → Market"):
            st.session_state.page = "market"
            st.rerun()


    # -------- IMPACT --------
    st.markdown('<div class="section-title">🌍 Impact</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card impact">
    ✔ Early detection of crop diseases <br>
    ✔ Smart weather-based decision alerts <br>
    ✔ Multilingual voice interaction <br>
    ✔ Profit-driven crop planning <br>
    ✔ Improves farmer productivity and income
    </div>
    """, unsafe_allow_html=True)