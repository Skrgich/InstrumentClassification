from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Flatten, Dense

model = Sequential()
model.add(Conv2D(32,(3,3)))


model.fit(use_multiprocessing= True, workers = 4)
model.pre
    
import numpy

x = numpy.empty((4,6))

numpy.insert(x, d)