from core.config import AI_PROVIDER

def run_prompt(prompt: str) -> str:
    if AI_PROVIDER == "mock":
        return f"[MOCK RESPONSE] You said: {prompt}"

    # future providers
    raise ValueError("AI provider not configured")
