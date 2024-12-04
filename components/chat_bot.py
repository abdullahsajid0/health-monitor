# chat_bot.py
import openai
import streamlit as st

# Initialize Groq (Replace with actual Groq integration)
def get_chat_response(user_input):
    # Example for Groq API interaction
    openai.api_key = "YOUR_API_KEY"
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=user_input,
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def chat(user_input):
    st.write("Bot: ", get_chat_response(user_input))
