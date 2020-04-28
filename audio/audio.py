import sounddevice as sd 
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import math
duration=5.0

fs=44100
myrecording=sd.rec(int(duration*fs),samplerate=fs,channels=2)



wavfile.write("output1.wav",fs,myrecording)

# arr=np.array(arr)
sd.wait()
print("recording finished")
sd.play(myrecording,fs)
sd.wait()
print("play over")
print("printing array")
print(myrecording)
print("===============================")
sample,data=wavfile.read('output1.wav')

print(data)




		


# print("playing converted audio")


# sd.play(myrecording,fs)
# sd.wait()

plt.show()

#e-i0



