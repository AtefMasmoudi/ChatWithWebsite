from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from chat import Chat
from utils import clean_text

import streamlit as st
st.title("Chat with any Website")
url_input=st.text_input("Enter a URL:")
query_input=st.text_input("Enter your message:")
submit_button=st.button("Submit")
if submit_button:
    loader = WebBaseLoader([url_input])
    data = clean_text(loader.load().pop().page_content[0:4000])
    chat=Chat()
    response=chat.extract_data(data,query_input)
    st.markdown(response.content,unsafe_allow_html=True)
