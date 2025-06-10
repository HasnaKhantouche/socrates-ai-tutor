import streamlit as st
from services.llm_service import get_socratic_response
from services.text_processor import preprocess_text
from services.ml_categorizer import categorize_question
import asyncio

st.set_page_config(page_title="Project Socrates", page_icon="🧠")

st.title("🧠 Project Socrates: Socratic Dialogue AI")
st.write("Ask a question and receive a Socratic response powered by Gemini and NLP.")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Your question:", key="input")

if st.button("Ask Socrates") and user_input.strip():
    with st.spinner("Thinking..."):
        processed = preprocess_text(user_input)
        complexity = categorize_question(user_input)
        # If get_socratic_response is async, use asyncio.run
        if asyncio.iscoroutinefunction(get_socratic_response):
            response = asyncio.run(get_socratic_response(user_input, complexity))
        else:
            response = get_socratic_response(user_input, complexity)
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Socrates", response))
        st.info(f"Complexity Level: {complexity}")

# Display chat history
for speaker, text in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Socrates:** {text}")