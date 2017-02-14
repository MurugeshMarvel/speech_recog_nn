import alsaaudio as al
import time
import audioop
import matplotlib.pyplot as plt



class input(object):
	def get_sound(self):
		self.ip = al.PCM(al.PCM_CAPTURE,al.PCM_NONBLOCK)
		self.ip.setchannels(1)
		self.ip.setrate(8000)
		self.ip.setformat(al.PCM_FORMAT_S16_LE)

		self.ip.setperiodsize(160)
		return self.ip.read()

	def save_sound(self,filename='test1'):
		i=0
		file_name = filename+'.txt'
		print file_name
		while True:
			self.fil = open(file_name,'a')
			inp = self.ip
			self.l,self.data = inp.read()
			if self.l :
				value = str(audioop.max(self.data,2))
				valu = str(i) + ','
				val = valu + value
				va = val + '\n'
				self.fil.write(va)
				print va
				time.sleep(.001)	
				i += 1

if __name__ == '__main__':
	obj = input()
	obj.get_sound()
	obj.save_sound(filename='test')