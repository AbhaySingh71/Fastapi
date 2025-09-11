from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
    
def test_loan_eligibility():    
    payload = {
            "income": 50000,
            "age": 21,
            "employment_status": "employed"
        }
    response = client.post('/loan-eligibility', json=payload)
    assert response.status_code == 200
    assert response.json() == {'eligible': True}
    
def test_fail_loan_eligibility():    
    payload = {
            "income": 40000,
            "age": 20,
            "employment_status": "unemployed"
        }
    response = client.post('/loan-eligibility', json=payload)
    assert response.status_code == 200
    assert response.json() == {'eligible': False}    
    
    