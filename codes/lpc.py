import speech_input as si
import numpy as np
#initialise the input parameter by calling the speech_input parameters
inp =   si.input()
inp.get_sound()

value = np.empty([0,0])
limit = input("Enter the time limit to record")
iteration = 0
while True:
	if (iteration<limit):
		value=np.append(value,int(inp.get_sound()))
	else:
		break
	iteration+=1


mean = np.mean(value) 	
print "The mean value is"
print mean
print "The standard Deviation is "
stand = np.std(value)
print stand
cons_value = value - mean
print ("the noise free value is %",cons_value)
min = np.min(value)
print min
 
print "Saved the feature vector fot RNN"

print "constructing frames"

no_of_frames = iteration/20
print "the iteration is", iteration

if ((iteration%20)!=0):
	frame_residue = iteration%20
	no_of_frames = no_of_frames+1

print type(value[2])
frame_length = 20
frame_value = np.empty((no_of_frames,frame_length))

frame_node = 0
for iter1 in range(0,no_of_frames):
	for iter2 in range(0,frame_length):
		
		if ((frame_node-(iteration-1)<=0)):
			frame_value[iter1][iter2] = value[frame_node]
			#print frame_node
		else:
			frame_value[iter1][iter2] = 0
		iter2+=1
		frame_node+=1
	iter1+=1

print "The Non-framed value is " 
print value

print "The Framed Value is"
print frame_value

print np.shape(frame_value)

print "The number of frames = ",no_of_frames
