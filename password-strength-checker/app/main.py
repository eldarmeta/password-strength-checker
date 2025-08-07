from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.checker import evaluate_password

app = FastAPI()

class PasswordInput(BaseModel):
    password: str

@app.post("/check-password")
def check_password(data: PasswordInput):
    score, strength, issues = evaluate_password(data.password)
    return {
        "score": score,
        "strength": strength,
        "issues": issues
    }