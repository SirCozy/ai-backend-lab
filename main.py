from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="AI Backend Lab Mock", version="0.1.0")

# Request model
class PromptRequest(BaseModel):
    prompt: str

# Response model
class PromptResponse(BaseModel):
    response: str

@app.get("/")
async def root():
    return {"message": "AI Backend Lab Mock is running!"}

@app.post("/prompt", response_model=PromptResponse)
async def run_prompt(request: PromptRequest):
    # Mock response – replace this with real API call later
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    
    mock_response = f"Mocked response for your prompt: '{request.prompt}'"
    return PromptResponse(response=mock_response)
