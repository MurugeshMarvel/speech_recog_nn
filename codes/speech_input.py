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
		
		
		while True:
			inp = self.ip
			l,data = inp.read()
			
			if l:
				sig = str(audioop.max(data,2))
				
				return sig
			time.sleep(.01)
			

	'''def save_sound(self,filename='test1'):
		i=0
		file_name = filename+'.txt'
		while True:
			self.fil = open(file_name,'w')
			inp = self.ip
			
			if self.l :
				value = str(audioop.max(self.data,2))
				valu = str(i) + ','
				val = valu + value
				va = val + '\n'
				self.fil.write(value)
				
				time.sleep(.001)	
				i += 1
				return value
'''

if __name__ == '__main__':
	obj = input()
	a = obj.get_sound()
	print a
	#obj.save_sound()
