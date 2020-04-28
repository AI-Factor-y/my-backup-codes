import pyaudio
import wave
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import math

sample,data=wavfile.read("audiofile.wav")
scaled_data=data[:,0]
scaled_data2=data[:,1]
scaled_data=scaled_data/2**15
scaled_data2=scaled_data2/2**15

print(scaled_data.shape)

def fourier(x,rot):
	transform=[]

	N=len(x)

	for k in range(N):
		real=0
		img=0

		for n in range(N):

			theta=2*math.pi*k*n/N

			real+=x[n]*math.cos(theta)
			img-=x[n]*math.sin(theta)

		real/=N
		img/=N

		freq=k
		amp=math.sqrt(real*real+img*img)

		phase=math.atan2(img,real)+rot

		transform.append([freq,amp,phase])

	return transform

dft=fourier(scaled_data,0)
print(dft)