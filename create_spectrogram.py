import matplotlib.pyplot as plt
import librosa.display
import numpy as np
from librosa import get_duration

def create_spectrogram(audio_file, image_name, image_format):

    y, sr = librosa.load(audio_file)
    n = 1
    if get_duration(y = y, sr = sr) > 6:
        n = int(get_duration(y = y, sr = sr) // 3)

    step = int(sr * get_duration(y = y, sr = sr) // n)
    print(step, n)
    
    for i in range(n):
        print(i * step , (i + 1) * step)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        ms = librosa.feature.melspectrogram(y = y[i * step : (i + 1) * step], sr = sr)
        log_ms = librosa.power_to_db(ms, ref=np.max)
        librosa.display.specshow(log_ms, sr=sr)

        fig.savefig(image_name + str(i) + image_format)
        plt.close(fig)

    return n
    
