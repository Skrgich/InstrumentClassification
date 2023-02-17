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
import keras.losses



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
    n = create_spectrogram(audio_file, 'temp', '.png')

    # print(2)
    ans = {inst: 0 for inst in INSTRUMENTS}
    # print(ans.keys())
    for i in range(n):
        x = np.array([image.img_to_array(image.load_img('temp{}.png'.format(i), target_size=(224, 224, 3)))])
        # print(x)
        # print(np.shape(x))  
        prediction = AI_MODEL.predict(x)
        # print(np.shape(prediction))
        # print(prediction)
        # ans = {}
        for i in range(len(INSTRUMENTS)):
            if prediction[0][i] > 0.4: ans[INSTRUMENTS[i]] += 1
            # else: ans[INSTRUMENTS[i]] = 0
        # print(ans)
    return ans

    y, sr = librosa.load(audio_file)
    return {"duration" : librosa.get_duration(y)}
    return {"filename": file.filename}

if __name__ == "__main__":
    app.run(debug = True)