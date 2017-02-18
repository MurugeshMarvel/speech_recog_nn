import speech_input as si
import numpy as np
from audiolazy import lpc

#initialise the input parameter by calling the speech_input parameters




class frames(object):
	
	def get_input(self):
		self.inp =   si.input()
		self.inp.get_sound()

		self.value = np.empty([0,0])
		self.word = raw_input("word you are going to speak")
		self.limit = input("Enter the time limit to record")

		self.iteration = 0
		while True:
			if (self.iteration<self.limit):
				self.value=np.append(self.value,int(self.inp.get_sound()))
			else:
				break
			self.iteration+=1


		mean = np.mean(self.value) 	
		print "The mean value is"
		print mean
		print "The standard Deviation is "
		stand = np.std(self.value)
		print stand
		cons_value = self.value - mean
		print ("the noise free value is %",cons_value)
		min = np.min(self.value)
		print min
	 
		print "Saved the feature vector fot RNN"

		return self.value
	def frame_segment(self,frame_size=20):
		print "constructing frames"
		self.frame_length = frame_size
		self.no_of_frames = self.iteration/self.frame_length
		print "the iteration is", self.iteration

		'''if ((iteration%20)!=0):
			frame_residue = self.iteration%20
			no_of_frames = no_of_frames+1'''

		self.frame_value = np.empty((self.no_of_frames,self.frame_length))

		frame_node = 0
		for iter1 in range(0,self.no_of_frames):
			for iter2 in range(0,self.frame_length):
				
				if ((frame_node-(self.iteration-1)<=0)):
					self.frame_value[iter1][iter2] = self.value[frame_node]
					#print frame_node
				else:
					self.frame_value[iter1][iter2] = 0
				iter2+=1
				frame_node+=1
			iter1+=1

		print "The Non-framed value is " 
		print self.value

		print "The Framed Value is"
		print self.frame_value

		print np.shape(self.frame_value)

		print "The number of frames = ",self.no_of_frames
		self.value_str = str(self.value)
		self.frame_value_str = str(self.frame_value)
		file_name = "data/"+self.word
		self.inp.save_sound(filename=file_name,value=self.value_str,frame=self.frame_value_str)	

	def lpc1(self,data,order):
		return lpc(data,order)





if __name__ == '__main__':
	frame_object = frames()
	inp = frame_object.get_input()
	frame_object.frame_segment(frame_size=30)
	lpc_value = frame_object.lpc1(inp,300)
	print "the length of the lpc value is ", len(lpc_value)
	print "the length of the origin value is ",len(inp)