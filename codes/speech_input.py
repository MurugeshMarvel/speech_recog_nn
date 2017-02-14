import alsaaudio as al
import time
import audioop
import matplotlib.pyplot as plt


ip = al.PCM(al.PCM_CAPTURE,al.PCM_NONBLOCK)

ip.setchannels(1)
ip.setrate(8000)
ip.setformat(al.PCM_FORMAT_S16_LE)

ip.setperiodsize(160)

i=0
while True:
	fil = open("sound_signal.txt",'a')
	l,data = ip.read()
	if l :
		value = str(audioop.max(data,2))
		valu = str(i) + ','
		val = valu + value
		va = val + '\n'
		fil.write(va)
		print va
	time.sleep(.001)	
	i += 1
