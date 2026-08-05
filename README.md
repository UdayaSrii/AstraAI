# AstraAI
# 🤖 AstraAI - Multimodal AI Assistant


![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Groq](https://img.shields.io/badge/Groq-Llama-orange)
![LangChain](https://img.shields.io/badge/LangChain-AI-green)


## 📌 Overview

PersonaAI is an intelligent AI assistant built using:

- Streamlit
- Groq Llama Models
- LangChain
- Retrieval Augmented Generation (RAG)

It allows users to chat with AI, upload PDFs, and ask questions from documents.


## ✨ Features

### 💬 AI Chat

- Fast responses using Groq Llama models
- Conversation memory
- Streaming responses


### 📄 PDF Question Answering

- Upload PDF documents
- Extract document knowledge
- Ask questions from files


### 💾 Chat Management

- Create multiple conversations
- Save chat history
- Export conversations


### ⚙️ Custom Controls

- Select AI model
- Adjust temperature
- Control response length

## 🏗️ Architecture

User
|
Streamlit UI
|
PersonaAI Backend
|

| | |
Groq LangChain RAG
LLM Memory PDF
|
Database



## 📂 Project Structure

AstraAI - Multimodal AI Assistant/

├── app.py

├── config/

├── core/

├── database/

├── auth/

├── utils/

├── uploads/

├── data/

└── requirements.txt
