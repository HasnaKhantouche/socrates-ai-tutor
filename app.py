import streamlit as st
import requests

st.set_page_config(page_title="Project Socrates", page_icon="🧠")

st.title("🧠 Project Socrates: Socratic Dialogue AI")
st.write("Ask a question and receive a Socratic response powered by Gemini and NLP.")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Your question:", key="input")

if st.button("Ask Socrates") and user_input.strip():
    with st.spinner("Thinking..."):
        # Call your FastAPI backend
        response = requests.post(
            "http://localhost:8000/dialogue",
            json={"question": user_input}
        )
        if response.status_code == 200:
            data = response.json()
            st.session_state.history.append(("You", user_input))
            st.session_state.history.append(("Socrates", data["response"]))
            st.info(f"Complexity Level: {data.get('complexity', 'N/A')}")
        else:
            st.error("Error: " + response.text)
    

# Display chat history
for speaker, text in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Socrates:** {text}")