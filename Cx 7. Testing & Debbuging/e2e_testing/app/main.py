from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Applicant(BaseModel):
    income: float
    age: int
    employement_status: str
    
@app.post("/loan_eligibility")
def check_loan_eligibility(applicant: Applicant):
    if (applicant.income >= 50000) and (applicant.age >= 21) and (applicant.employement_status == "employed"):
        return {"eligible": True}
    else:
        return {"eligible": False}
    
    