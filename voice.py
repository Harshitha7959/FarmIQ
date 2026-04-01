import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from openai import OpenAI
import os

# -------- SET YOUR API KEY --------
client = OpenAI(api_key="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")  # 🔥 Replace this

# -------- AI RESPONSE --------
def get_ai_response(text):

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert smart farming assistant. Give short and practical answers."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content

    except:
        return "Sorry, AI service is not available."


# -------- TEXT TO SPEECH --------
def speak(text, lang):

    try:
        if lang == "Kannada":
            tts = gTTS(text=text, lang='kn')
        else:
            tts = gTTS(text=text, lang='en')

        filename = "response.mp3"
        tts.save(filename)

        audio_file = open(filename, "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

    except:
        st.error("Voice output failed")


# -------- MAIN UI --------
def show():

    st.markdown("<h2>🎤 AI Voice Assistant</h2>", unsafe_allow_html=True)

    lang = st.selectbox("🌐 Select Language", ["English", "Kannada"])

    if st.button("🎤 Speak"):

        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                st.info("🎤 Listening... Speak clearly")

                # 🔥 FIXED PART
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=7)

            # -------- SPEECH TO TEXT --------
            if lang == "Kannada":
                text = r.recognize_google(audio, language="kn-IN")
            else:
                text = r.recognize_google(audio, language="en-IN")

            st.success(f"You said: {text}")  # optional (remove if not needed)

            # -------- AI RESPONSE --------
            response = get_ai_response(text)

            # -------- VOICE OUTPUT --------
            speak(response, lang)

        except sr.UnknownValueError:
            speak("I could not understand. Please speak clearly.", lang)

        except sr.RequestError:
            speak("Speech service is not available.", lang)

        except Exception as e:
            speak("Something went wrong. Please try again.", lang)