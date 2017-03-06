import matplotlib.pyplt as plt
import numpy as np
from statistics import mean
import wave
import sys

plt.figure(1)

class Audio:
	def __init__(self,audio):
		self.audio = wave.open(audio,'r')
		self.signal = self.audio.readframes(-1)
		self.signal = np.fromstring(self.signal, 'Int16')
		self.fr = self.audio.getframerate()
		self.time = np.linspace(0,100,num=(len(self.signal)))
		self.fft = np.fft.fft(self.signal)

	sef plot(self):
	plt.title('Audio Waveforms')
	plt.plot(self.time,self.signal,'.')

gana = Audio('gana.wav')
gane = Audio('hmm.wav')
gana.plot()
hmm.plot()
plt.show()