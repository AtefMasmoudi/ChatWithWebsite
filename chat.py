import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")

class Chat:
    def __init__(self):
        self.chat=ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="llama-3.3-70b-versatile")
    
    def extract_data(self,text_from_website,text_from_user):
        prompt_extract=PromptTemplate.from_template(
        """
        ### Scrapped text from website
        {page_data}
        ### Instruction
        Your job is to respond to the {query} entered by the user
        """
        )
        chain_extract=prompt_extract | self.chat
        response=chain_extract.invoke(input={"page_data":text_from_website,"query":text_from_user})    
        return response