# app.py
import streamlit as st
from auth import sign_up, sign_in
from chat_bot import chat
from vader_analysis import analyze_sentiment

# Authentication Section
def authentication():
    st.title("Welcome to the Legal Help Desk")
    auth_mode = st.sidebar.radio("Choose action", ["Sign Up", "Log In"])

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if auth_mode == "Sign Up":
        if st.button("Sign Up"):
            sign_up(email, password)
    elif auth_mode == "Log In":
        if st.button("Log In"):
            sign_in(email, password)

# Chatbot Section
def chatbot_section():
    st.title("Legal Help Desk Chatbot")

    user_input = st.text_input("Ask a question about legal matters")

    if user_input:
        st.write(f"You: {user_input}")
        
        # Sentiment Analysis
        sentiment = analyze_sentiment(user_input)
        st.write(f"Sentiment: {sentiment}")

        # Bot Response
        chat(user_input)

if __name__ == "__main__":
    authentication()
    chatbot_section()
