from fastapi import FastAPI, File, UploadFile
import uvicorn
import librosa
import io
import os
import keras.utils as image
from funkcije import create_spectrogram
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np


INSTRUMENTS = ["cel", "cla", "flu", "gac", "gel", "org", "pia", "sax", "tru", "vio", "voi"]
MODEL_PATH = 'Model'
AI_MODEL = None

app = FastAPI()

@app.on_event("startup")
def on_startup():
    global AI_MODEL
    if os.path.exists(MODEL_PATH):
        AI_MODEL = load_model(MODEL_PATH)


@app.get('/')
def home():
    return {"Data" : "test"}

@app.post("/upload")
async def upload_file(file: UploadFile):
    audio_bytes = await file.read()
    audio_file = io.BytesIO(audio_bytes)

    # print(1)

    create_spectrogram(audio_file, 'temp.png')

    # print(2)

    x = np.array([image.img_to_array(image.load_img('temp.png', target_size=(224, 224, 3)))])

    # print(np.shape(x))  
    prediction = AI_MODEL.predict(x)
    # print(np.shape(prediction))
    ans = {}
    for i in range(len(INSTRUMENTS)):
        if prediction[0][i] > 0.3: ans[INSTRUMENTS[i]] = 1
        else: ans[INSTRUMENTS[i]] = 0
    return ans

    y, sr = librosa.load(audio_file)
    return {"duration" : librosa.get_duration(y)}
    return {"filename": file.filename}

if __name__ == "__main__":
    app.run(debug = True)