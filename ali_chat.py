import streamlit as st
from openai import OpenAI
import os

# Load API key securely from Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit page configuration
st.set_page_config(page_title="💬 Chat with Ali 🤖✨", page_icon="🌿")
st.title("💬 Ali - Your Aligned Growth Guide 🌿")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hey there! Ali here—ready to align your growth. 🌱✨ What do you need help with today?"}
    ]

# Display chat messages
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input("Type your question here..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.spinner("Ali is thinking... 🤔"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state["messages"]],
        )
        msg_content = response.choices[0].message.content
        st.session_state["messages"].append({"role": "assistant", "content": msg_content})
        st.chat_message("assistant").write(msg_content)