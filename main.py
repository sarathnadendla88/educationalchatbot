import streamlit as st
from agents.educational_chatbot import get_educational_llm
from utils.session import init_session, add_user_message, add_bot_message, get_chat_history
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="Educational Guidance Chatbot", page_icon="🎓")
st.title("🎓 Ask Your Educational Guide")

init_session()
llm = get_educational_llm()

user_input = st.chat_input("Ask me anything about courses, careers, or exams after 12th...")

if user_input:
    add_user_message(user_input)
    history = [HumanMessage(content=m["content"]) for m in get_chat_history() if m["role"] == "user"]
    response = llm(history)
    add_bot_message(response.content)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])