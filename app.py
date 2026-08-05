import streamlit as st
import os
import time


from core.groq_client import generate_response

from core.rag import create_pdf_database

from database.chat_db import (
    create_database,
    create_chat,
    save_message,
    get_messages,
    get_user_chats
)

from utils.helpers import export_chat



# =====================================
# Page Config
# =====================================

st.set_page_config(

    page_title="AstraAI",

    page_icon="🤖",

    layout="wide"

)



# =====================================
# Database
# =====================================

create_database()



# =====================================
# Session
# =====================================

if "user" not in st.session_state:

    st.session_state.user = "demo@gmail.com"



if "chat_id" not in st.session_state:

    st.session_state.chat_id = None



if "vector_db" not in st.session_state:

    st.session_state.vector_db = None



# =====================================
# Header
# =====================================


st.title(
    "🤖 AstraAI"
)


st.caption(
    "Your AstraAI - Multimodal AI Assistant powered by Groq Llama"
)



# =====================================
# Sidebar
# =====================================


st.sidebar.title(
    "⚙️ Settings"
)



model = st.sidebar.selectbox(

    "Model",

    [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant"
    ]

)



temperature = st.sidebar.slider(

    "Temperature",

    0.0,

    1.0,

    0.7

)



max_tokens = st.sidebar.slider(

    "Max Tokens",

    100,

    4096,

    1024

)



# =====================================
# Chat Management
# =====================================


if st.sidebar.button(
    "➕ New Chat"
):

    chat_id = create_chat(

        st.session_state.user,

        "New Conversation"

    )


    st.session_state.chat_id = chat_id


    st.rerun()



st.sidebar.subheader(
    "Previous Chats"
)


chats = get_user_chats(
    st.session_state.user
)



for chat in chats:

    if st.sidebar.button(
        chat[1],
        key=chat[0]
    ):

        st.session_state.chat_id = chat[0]

        st.rerun()



# =====================================
# PDF Upload
# =====================================


pdf = st.sidebar.file_uploader(

    "📄 Upload PDF",

    type="pdf"

)



if pdf:


    os.makedirs(
        "uploads",
        exist_ok=True
    )


    path = (
        "uploads/"
        +
        pdf.name
    )


    with open(
        path,
        "wb"
    ) as f:

        f.write(
            pdf.getbuffer()
        )


    with st.spinner(
        "Reading PDF..."
    ):

        st.session_state.vector_db = (
            create_pdf_database(path)
        )


    st.sidebar.success(
        "PDF Loaded"
    )



# =====================================
# Load Messages
# =====================================


messages=[]


if st.session_state.chat_id:


    messages = get_messages(

        st.session_state.chat_id

    )



# =====================================
# Display Chat
# =====================================


for message in messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )



# =====================================
# Chat Input
# =====================================


prompt = st.chat_input(
    "Ask something..."
)



if prompt:


    if not st.session_state.chat_id:

        st.session_state.chat_id = create_chat(

            st.session_state.user,

            prompt[:30]

        )



    save_message(

        st.session_state.chat_id,

        "user",

        prompt

    )


    with st.chat_message(
        "user"
    ):

        st.markdown(prompt)



    api_messages = [

        {
            "role":"system",
            "content":
            """
            You are AstraAI.
            Answer professionally.
            """
        }

    ]


    api_messages.extend(

        get_messages(

            st.session_state.chat_id

        )

    )



    with st.chat_message(
        "assistant"
    ):

        box = st.empty()

        answer=""


        start=time.time()


        stream = generate_response(

            api_messages,

            model,

            temperature,

            max_tokens

        )


        for chunk in stream:

            if chunk.choices[0].delta.content:

                answer += (
                    chunk
                    .choices[0]
                    .delta
                    .content
                )


                box.markdown(
                    answer+"▌"
                )


        box.markdown(
            answer
        )


        st.caption(
            f"Response time: {round(time.time()-start,2)}s"
        )



    save_message(

        st.session_state.chat_id,

        "assistant",

        answer

    )



# =====================================
# Export
# =====================================


if st.sidebar.button(
    "⬇ Export Current Chat"
):


    st.sidebar.download_button(

        "Download",

        export_chat(messages),

        "chat.json"

    )



st.divider()

st.caption(
    "Built with Streamlit + Groq + LangChain"
)