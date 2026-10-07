# AI FAQ Chatbot

A simple AI-powered FAQ chatbot for answering college-related questions using RAG (Retrieval-Augmented Generation).

## Features

- Answers college FAQ questions
- Uses FAISS for similarity search
- Uses HuggingFace embeddings
- Uses Gemini for generating answers
- Provides a FastAPI REST API
- Swagger UI for testing the API

## Technologies Used

- Python
- FastAPI
- LangChain
- Gemini
- FAISS
- HuggingFace
- Sentence Transformers

## How It Works

1. FAQ data is stored in the application.
2. Questions and answers are converted into embeddings.
3. FAISS searches for relevant information.
4. The retrieved information is given to Gemini.
5. Gemini generates the final answer.

## Project Structure

```text
ai-faq-chatbot/
│
├── api.py
├── chatbot.py
├── embeddings.py
├── faq_data.py
├── vector_store.py
├── requirements.txt
└── .gitignore
