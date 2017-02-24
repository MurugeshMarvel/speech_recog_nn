import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.io import wavfile
import scipy
fpaths = []
labels = []
spoken = []

for f in os.listdir('audio'):
	for w in os.listdir('audio/' + f):
		fpaths.append('audio/' + f + '/' + w)
		labels.append(f)
		if f not in spoken:
			spoken.append(f)
print ('words spoken',spoken)

data = np.zeros((len(fpaths), 32000))
maxsize = -1
for n, file in enumerate(fpaths):
	_,d = wavfile.read(file)
	data[n, :d.shape[0]] = d
	if d.shape[0] > maxsize:
		maxsize = d.shape[0]

data = data[:, :maxsize]

print('Number of files total', data.shape[0])
all_labels = np.zeros(data.shape[0])
for n, l in enumerate(set(labels)):
	all_labels[np.array([i for i, _ in enumerate(labels) if _ == l])] = n

print ('Labels and label indices', all_labels)

def stft(x, fftsize = 64, overlap_pct = 5):
	hop = int(fftsize *(1-overlap_pct))
	w = scipy.hanning(fftsize + 1)[:-1]
	raw = np.array([np.fft.rfft(w * x[i:i + fftsize]) for i in range(0, len(x) - fftsize,hop)])
	return raw[:,(fftsize // 2)]

plt.plot(data[0, :],color='steelblue')
plt.title('Timeseries examples for %s'%labels[0])
plt.xlim(0, 3500)
plt.xlabel('Time (Samples)')
plt.ylabel('Amplitude (Signal 16 bit)')
plt.figure()

log_freq = 20 * np.log(np.abs(stft(data[0, :]))+ 1)
print "log_freq.shape"
plt.imshow(log_freq.shape)
plt.xlabel("Freq(bin)")
plt.ylabel("Time (Overlapped Frames)")
plt.ylim(log_freq.shape[1])
plt.title('PSD of %s example' %labels[0])
