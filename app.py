import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Text Summarizer", page_icon="📝")

st.title("📝 AI Text Summarizer")
st.caption("A simple AI-powered text summarization app built with Python and Streamlit.")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.warning("Add your OPENAI_API_KEY as an environment variable before using the app.")
    st.code('$env:OPENAI_API_KEY="your_api_key_here"')
    st.stop()

client = OpenAI(api_key=api_key)

text = st.text_area("Paste text to summarize", height=300, placeholder="Paste an article, notes, or any long text here...")

style = st.selectbox("Summary style", ["Concise", "Bullet points", "Detailed"])

if st.button("Summarize", type="primary"):
    if not text.strip():
        st.error("Please paste some text first.")
    else:
        prompt = f"""Summarize the following text in a {style.lower()} style.
Keep the important facts and make the result easy to read.

TEXT:
{text[:20000]}"""

        with st.spinner("Generating summary..."):
            response = client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
                messages=[{"role": "user", "content": prompt}],
            )

        st.subheader("Summary")
        st.write(response.choices[0].message.content)
