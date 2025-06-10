# Project Socrates: AI Socratic Dialogue Tutor

Project Socrates is an open-source EdTech application that simulates Socratic dialogue to foster critical thinking. Powered by FastAPI, Streamlit, and Google Gemini, it guides users through thoughtful questioning, never giving direct answers, and adapts its approach based on question complexity using NLP and a decision tree model.

## Features

- **Socratic Dialogue:** AI responses scaffold deeper understanding, challenge assumptions, and encourage reflection.
- **Critical Thinking Focus:** Designed for educational use, with safeguards against harmful or biased content.
- **NLP Preprocessing:** Tokenization, lemmatization, and claim detection to focus Socratic questioning.
- **Complexity Categorization:** ML-based decision tree adapts dialogue depth to user input.
- **Modern UI:** Streamlit frontend for easy, interactive use.
- **Easy Deployment:** Ready for Streamlit Cloud (recommended), Fly.io, Railway, or Deta Space.

## Quick Start

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/project-socrates-ai-tutor.git
   cd project-socrates-ai-tutor
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key:**
   - Create a `.env` file with your Google Gemini API key:
     ```
     GOOGLE_API_KEY=your_key_here
     ```

4. **Run the backend:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Run the frontend:**
   ```bash
   streamlit run app.py
   ```

6. **Test the API:**
   ```bash
   pytest
   ```

## Deployment

- **Recommended:** [Streamlit Cloud](https://streamlit.io/cloud)  
  - Connect your GitHub repo, set `app.py` as the entry point, and add your API key as a secret.

## License

MIT License

---

**Built for Valearnis and all educators who believe in the power of questioning.**