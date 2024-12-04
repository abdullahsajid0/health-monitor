# chat_bot.py
import os
import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Function to get the chat response from Groq
def get_chat_response(user_input):
    # Groq API call to get the response
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="lllama-3.2-90b-vision-preview",
    )

    return chat_completion.choices[0].message.content

# Function to display the chat response on Streamlit
def chat(user_input):
    response = get_chat_response(user_input)
    st.write(f"Bot: {response}")
