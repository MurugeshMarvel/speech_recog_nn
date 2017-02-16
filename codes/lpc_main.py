import soundfile as sf
import scipy.signal as scisig
import numpy as np

data, fs = sf.read("speech2.wav")

data_len =  len(data)
#data_resam = scisig.resample(data,8000)

max_data= max(abs(data))
#print max_data
data_norm = np.array([])

for i in range(0,(data_len-1)):
	data_norm = np.append(data_norm,0.9*data[i]/max_data)


print data_norm[0]
print data_norm[1]
print data_norm[2]

print fs
print data[50000]