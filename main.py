from fastapi import FastAPI, File, UploadFile
import uvicorn
import librosa
import io

app = FastAPI()

@app.get('/')
def home():
    return {"Data" : "test"}

@app.post("/upload")
async def upload_file(file: UploadFile):
    audio_bytes = await file.read()
    audio_file = io.BytesIO(audio_bytes)

    y, sr = librosa.load(audio_file)
    return {"duration" : librosa.get_duration(y)}
    return {"filename": file.filename}

if __name__ == "__main__":
    app.run(debug = True)