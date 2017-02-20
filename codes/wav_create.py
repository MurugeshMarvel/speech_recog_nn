from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave


threshold = 8000
chunk_size = 1024
form = pyaudio.paInt16
rate = 44100

def is_silent(snd_data):
	'''return true if below the 'silent' threshold'''
	return max(snd_data) < threshold

def normalise(snd_data):
	'''Average the volume out'''
	maxi = 16384
	times = float(maxi)/max(abs(i)for i in snd_data)

	r = array('h')
	for i in snd_data:
		r.append(int(i*times))
	return r

def trim(snd_data):
	'''Trim the blank spots at the start and end'''
	def _trim(snd_data):
		snd_started = False
		r = array('h')

		for i in snd_data:
			if not snd_started and abs(i) > threshold:
				snd_started = True
				r.append(i)

			elif snd_started:
				r.append(i)

		return r

	snd_data = _trim(snd_data)

	snd_data.reverse()
	snd_data = _trim(snd_data)
	snd_data.reverse()

	return snd_data

def add_silence(snd_data, seconds):
	'''Adding silence to the start and end of the snd_data of the length seconds(float)'''
	r = array('h',[0 for i in range(int(seconds*rate))])
	r.extend(snd_data)
	r.extend([0 for i in range(int(seconds*rate))])
	return r


def record():
	aud = pyaudio.PyAudio()
	stream = aud.open(format=form, channels=1,rate=rate,input=True,output=True,frames_per_buffer=chunk_size)
	num_silent = 0
	snd_started = False
	r = array('h')
	while True:
		#little Endian, signed short
		snd_data = array('h',stream.read(chunk_size))
		if byteorder == 'big':
			snd_data.byteswap()
		r.extend(snd_data)

		silent = is_silent(snd_data)

		if silent and snd_started:
			num_silent +=1

		elif not silent and not snd_started:
			snd_started = True

		if snd_started and num_silent > 30:
			break

	sample_width = aud.get_sample_size(form)
	stream.stop_stream()
	stream.close()
	aud.terminate()

	r = normalise(r)
	r = trim(r)
	r = add_silence(r,0.5)
	return sample_width,r

def record_to_file(path):
	sample_width, data = record()
	data= pack('<' + ('h'*len(data)), *data)

	wf = wave.open(path, 'wb')
	wf.setnchannels(1)
	wf.setsampwidth(sample_width)
	wf.setframerate(rate)
	wf.writeframes(data)
	wf.close()


if __name__ == "__main__":
	print "please speak a word into the microphone"
	record_to_file('demo1.wav')
	print "done- result has been written in demo1.wav"
