# Chat with Any Website

This project allows users to chat with any website by extracting content from the provided URL and processing it with an AI model using **Groq Cloud**'s API. The application is built with **Streamlit** for the frontend and **LangChain** for integrating the language model.

## Prerequisites

Before running the application, you need to make sure you have the following:

- **Python 3.8+**
- **An active account on GroqCloud** to get your **API Key**.

## Setup Instructions

### 1. Create a Python Virtual Environment

First, navigate to your project directory in the terminal or command prompt.

#### **Create the virtual environment:**
```bash
python3 -m venv venv
.
├── main.py               # Main Streamlit app to interact with the website
├── chat.py               # Contains logic for extracting and responding to user queries
├── utils.py              # Utility functions (like `clean_text` for cleaning extracted data)
├── requirements.txt      # List of required Python packages
├── .env                  # Environment file for API keys
└── README.md             # This readme file
