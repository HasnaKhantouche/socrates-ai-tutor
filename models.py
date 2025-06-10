from pydantic import BaseModel
from typing import Optional

class DialogueRequest(BaseModel):
    question: str

class DialogueResponse(BaseModel):
    response: str
    processed_input: str