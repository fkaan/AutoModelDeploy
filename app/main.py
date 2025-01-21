from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from app.model_handler import load_model, run_inference
import os
import pandas as pd

app = FastAPI()

UPLOAD_DIR = "models"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return HTMLResponse(content=open("app/templates/upload_form.html").read())

@app.post("/upload-model/")
async def upload_model(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as f :
        f.write(await file.read())
    return {"message" : f"Model saved at {file_location}"}

@app.post("/upload-data/")
async def upload_data(file: UploadFile = File(...)):
    data = pd.read_csv(file.file)
    model_path = f"{UPLOAD_DIR}/model.pkl"
    if not os.path.exists(model_path):
        return {"error": "No model found. Please upload a model first."}

    # Run inference
    predictions = run_inference(model_path, data)
    return {"predictions": predictions.tolist()}



