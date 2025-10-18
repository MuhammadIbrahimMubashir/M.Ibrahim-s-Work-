import os
import streamlit as st
import google.generativeai as genai

# Set service account key path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gemini-key.json"

# Configure Gemini
genai.configure()

# Load the Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = model.start_chat(history=[])

# Streamlit page config
st.set_page_config(page_title="💬 Chatbot Agentic AI - Muhammad Ibrahim Mubashir", page_icon="🤖")
st.title("🤖 Gemini Chatbot - By Muhammad Ibrahim Mubashir")

# Session state to keep chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input box
user_input = st.chat_input("💡 Type your message here...")

if user_input:
    # Show user's message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get Gemini response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            response = chat.send_message(user_input)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
