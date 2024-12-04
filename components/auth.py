# auth.py
import firebase_admin
from firebase_admin import auth
import streamlit as st

def sign_up(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        st.success(f"User {email} created successfully!")
        return user
    except Exception as e:
        st.error(f"Error signing up: {e}")

def sign_in(email, password):
    try:
        user = auth.get_user_by_email(email)
        st.success(f"Welcome back, {email}!")
        return user
    except Exception as e:
        st.error(f"Error signing in: {e}")
