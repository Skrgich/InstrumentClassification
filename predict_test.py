import io
import os
import json
import keras.utils as image
import numpy as np
from funkcije import create_spectrogram
from keras.models import load_model


INSTRUMENTS = ["cel", "cla", "flu", "gac", "gel", "org", "pia", "sax", "tru", "vio", "voi"]
MODEL_PATH = 'Model_final'
AI_MODEL = load_model(MODEL_PATH)


folder_path = "test_dataset"

test_prediction = {}

for filename in os.listdir(folder_path):
    if filename[-4:] != '.wav': 
        continue

    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        with open (file_path, 'rb') as f:
            audio_bytes = f.read()
        audio_file = io.BytesIO(audio_bytes)

        n = create_spectrogram(audio_file, 'temp', '.png')

        ans = {inst : 0 for inst in INSTRUMENTS}

        for i in range(n):
            x = np.array([image.img_to_array(image.load_img('temp{}.png'.format(i), target_size=(224, 224, 3)))])
            
            prediction = AI_MODEL.predict(x)

            for i in range(len(INSTRUMENTS)):
                if prediction[0][i] > 0.5:
                    ans[INSTRUMENTS[i]] = 1

        test_prediction[filename[:-4]] = ans.copy()            

with open("test_labels.json", "w") as f:
    json.dump(test_prediction, f, indent = 4)
