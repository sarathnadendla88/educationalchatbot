import streamlit as st

def init_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def add_user_message(content):
    st.session_state.messages.append({"role": "user", "content": content})

def add_bot_message(content):
    st.session_state.messages.append({"role": "assistant", "content": content})

def get_chat_history():
    return [
        {"role": msg["role"], "content": msg["content"]} 
        for msg in st.session_state.messages
    ]