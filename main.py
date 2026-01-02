from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/prompt")
def run_prompt(data: PromptRequest):
    text = data.prompt
    return {
        "received": text,
        "length": len(text)
    }
