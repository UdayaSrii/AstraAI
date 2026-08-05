import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()


def get_groq_key():

    try:
        return st.secrets["GROQ_API_KEY"]

    except Exception:

        return os.getenv(
            "GROQ_API_KEY"
        )



def get_config():

    return {

        "model":
        "llama-3.3-70b-versatile",

        "temperature":
        0.7,

        "max_tokens":
        2048

    }