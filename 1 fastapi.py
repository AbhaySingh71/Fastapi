from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message': Hello world}


@app.get('/about')
def about():
    return {'message': 'I am a data entusatic and passonaite about to learn new things'}    