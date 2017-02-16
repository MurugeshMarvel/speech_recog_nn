import soundfile as sf
import scipy.signal as scisig
import numpy as np
import matplotlib.pyplot as plt
data, fs = sf.read("speech2.wav")

data_len =  len(data)


max_data= max(abs(data))
#print max_data
data_norm = np.array([])

for j in range(0,data_len):
	data_norm = np.append(data_norm,0.9*data[j]/max_data)

print j


data_resam = scisig.resample(data_norm,8000)

data_resam_len = len(data_resam)
print "The first five normalised data is"
for i in range(0,5):
	print data_norm[i]

print "The first five resamples data are"

for i in range(0,5):
	print data_resam[i]


'''plt.plot(data_len,data_norm,'go-',data_resam_len,data_resam,'.-')
pl.legend(['data','resampled'],loc='best')
plt.show()'''
print len(data_resam)

print "the shape of the data_norm"
print np.shape(data_norm)
print "the shape of the resamples data"
print np.shape(data_resam)