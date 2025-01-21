import joblib
import pandas as pd

def load_model(model_path: str):
    #load saved model
    return joblib.load(model_path)


def run_inference(model_path: str, data: pd.DataFrame):
    #run inference using the loaded model
    model = load_model(model_path)
    predictions = model.predict(data)
    return predictions