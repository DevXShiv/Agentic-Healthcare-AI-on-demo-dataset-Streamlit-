from fastapi import FastAPI
from pydantic import BaseModel
from agentic_ai import agentic_ai_predict  # fixed import

app = FastAPI()

# Define expected input
class SymptomInput(BaseModel):
    fever: int
    cough: int
    fatigue: int
    headache: int
    chest_pain: int
    sob: int
    diarrhea: int
    nausea: int
    dizziness: int
    sore_throat: int

@app.get("/")
def root():
    return {"message": "Healthcare Agentic AI is running 🚀"}

@app.post("/predict")
def predict_symptoms(input_data: SymptomInput):
    # Convert input to dict
    user_input = input_data.dict()
    # Get prediction from agentic_ai
    result = agentic_ai_predict(user_input)
    return result
