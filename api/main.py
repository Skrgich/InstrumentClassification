from fastapi import FastAPI, File, UploadFile
import uvicorn
import librosa
import io
import os
import keras.utils as image
from create_spectrogram import create_spectrogram
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import keras.losses



INSTRUMENTS = ["cel", "cla", "flu", "gac", "gel", "org", "pia", "sax", "tru", "vio", "voi"]
MODEL_PATH = 'Model_final'
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

    n = create_spectrogram(audio_file, 'temp', '.png')

    ans = {inst: 0 for inst in INSTRUMENTS}

    for i in range(n):
        x = np.array([image.img_to_array(image.load_img('temp{}.png'.format(i), target_size=(224, 224, 3)))])
      
        prediction = AI_MODEL.predict(x)
        
        for i in range(len(INSTRUMENTS)):
            if prediction[0][i] > 0.4: ans[INSTRUMENTS[i]] += 1

    return ans

    # y, sr = librosa.load(audio_file)
    # return {"duration" : librosa.get_duration(y)}
    # return {"filename": file.filename}

if __name__ == "__main__":
    app.run(debug = True)