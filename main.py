from fastapi import FastAPI, Request, HTTPException
from models import DialogueRequest, DialogueResponse
from services.llm_service import get_socratic_response
from services.text_processor import preprocess_text
from services.ml_categorizer import categorize_question

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Project Socrates API is running."}

@app.post("/dialogue")
async def dialogue(request: DialogueRequest) -> DialogueResponse:
    try:
        processed = preprocess_text(request.question)
        complexity = categorize_question(request.question)
        response = await get_socratic_response(request.question, complexity)
        return DialogueResponse(
            response=response,
            processed_input=processed,
            user_input_complexity=complexity
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))