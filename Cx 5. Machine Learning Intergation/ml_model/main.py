from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from typing import List
from predict import make_prediction, make_batch_predictions

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Housing Price Prediction API"}

@app.post("/predict", response_model=OutputSchema)
def predict_price(input_data: InputSchema):
    prediction = make_prediction(input_data.model_dump())
    return OutputSchema(predicted_price=prediction)

@app.post('/batch_prediction', response_model=List[OutputSchema])
def batch_predict(user_inputs: List[InputSchema]):
    predictions = make_batch_predictions([x.model_dump() for x in user_inputs])
    return [OutputSchema(predicted_price=round(prediction, 2)) for prediction in predictions]