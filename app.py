TITLE = 'Gemini AI Lab'
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
st.set_page_config(page_title=TITLE, page_icon="🎓")
st.title(TITLE)
st.caption("Shubham Prasad | 202510101110125 | SRMU | B.Tech CSE")
from google import genai

question = st.text_area("Ask Gemini a question")
if st.button("Get answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    elif not os.getenv("GEMINI_API_KEY"):
        st.error("Add GEMINI_API_KEY to your .env file.")
    else:
        try:
            client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
            response = client.models.generate_content(model="gemini-3.5-flash-lite", contents=question)
            st.write(response.text or "No text response returned.")
        except Exception as error:
            st.error(f"Request failed: {error}")
