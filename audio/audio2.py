import pyaudio
import wave
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np


#part recording
chunk=1024
sample_format=pyaudio.paInt16
filename="audiofile.wav"
channels=2
fs=44100
seconds=1

p=pyaudio.PyAudio()

print("recording")

stream=p.open(format=sample_format,channels=channels,rate=fs,frames_per_buffer=chunk,input=True)

frames=[]
for i in range(0,int(fs/chunk*seconds)):
	data=stream.read(chunk)
	frames.append(data)

stream.stop_stream()
stream.close()

p.terminate()

print("recording finished")

wf=wave.open(filename,'wb')

wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

#part opening======================================================
sample,data=wavfile.read("audiofile.wav")
# part scaling=====================================================
scaled_data=data[:,0]
scaled_data2=data[:,1]
scaled_data=scaled_data/2**15
scaled_data2=scaled_data2/2**15

# part ploting amp vs time==========================================
plt.plot(scaled_data)   # plotting mono left======================
plt.show()
plt.plot(scaled_data2)  # plotting mono right=====================
plt.show()

# ploting spectrogram==============================================
spectrum, freqs, t, im = plt.specgram(scaled_data, Fs=fs, NFFT=1024, cmap=plt.get_cmap('autumn_r'))

cbar = plt.colorbar(im)

plt.xlabel('Time (s)')

plt.ylabel('Frequency (Hz)')

cbar.set_label('Intensity (dB)')

plt.show()

#printing mono left==================================================
print(scaled_data)
# print(spectrum)

#decibel factors of sound===========================================
# scaled_data=10*np.log10(scaled_data)
# spectrum=10*np.log10(spectrum)
# plt.plot(spectrum)
# plt.show()

#trimming sound===================================================
start=1
end=1
trimmed=data[fs*start:fs*end]

#revebration time of a specific frequency in the sound===================================
