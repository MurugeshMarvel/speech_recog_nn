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
			

	def save_sound(self,filename,value,frame):
		file_name = filename + ".txt"
		file = open(file_name,'w')
		self.initial_value = value
		self.initial_frame = frame
		file.write("#################################")
		file.write("\n The Value is ")
		file.write(value)
		file.write("\n The frames are")
		file.write(frame)
		file.write("END")
		file.close()
		print "values saved in file",file_name


if __name__ == '__main__':
	obj = input()
	a = obj.get_sound()
	print a
	#obj.save_sound()
