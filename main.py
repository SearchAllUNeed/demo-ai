from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from adapter import run_model

app = FastAPI()

class Request(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", encoding="utf-8") as f:
        return f.read()

@app.post("/predict")
def predict(req: Request):
    result = run_model(req.text)
    return {"result": result}