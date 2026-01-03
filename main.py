from fastapi import FastAPI
from pydantic import BaseModel
from services.ai_service import run_prompt

app = FastAPI(title="AI Backend Lab")

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/prompt")
def prompt_ai(data: PromptRequest):
    response = run_prompt(data.prompt)
    return {"response": response}
