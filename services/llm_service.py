import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

system_prompt = """
You are Socrates, an AI tutor developed by Valearnis. Your role is to:
1. Stimulate critical examination of ideas
2. Guide users to discover answers themselves
3. Progress complexity based on user responses
4. NEVER give direct answers
5. Safeguard against harmful content

Response template:
- Start with clarifying question
- Challenge one assumption
- Suggest alternative perspective
- End with open-ended reflection question
"""

async def get_socratic_response(user_input: str, complexity: int) -> str:
    # Adjust prompt depth based on complexity
    if complexity == 1:
        depth = "Ask a simple clarifying question and suggest a basic alternative perspective."
    elif complexity == 2:
        depth = "Challenge an assumption and suggest a nuanced alternative perspective."
    else:
        depth = "Challenge multiple assumptions, suggest advanced perspectives, and end with a deep open-ended question."
        
    prompt = f"{system_prompt}\nUser: \"{user_input}\"\nSocrates:"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Gemini API error:", str(e))  # Add this line for debugging
        if "rate limit" in str(e).lower():
            return "Hmm, my thoughts are crowded today. Could you rephrase that?"
        if "content" in str(e).lower():
            return "Let's explore a different perspective. What if we consider..."
        return f"An error occurred: {str(e)}"