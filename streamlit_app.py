import streamlit as st

from src.rag import build_vector_db
from src.agent import run_agent

st.title("saftey bot")

st.write("Ask questions about construction safety data.")

# Build vector database once
@st.cache_resource
def load_db():
    return build_vector_db()

db = load_db()

question = st.text_input("Ask a question:")

if question:
    with st.spinner("Thinking..."):
        answer = run_agent(question, db)

    st.subheader("Answer")
    st.write(answer)