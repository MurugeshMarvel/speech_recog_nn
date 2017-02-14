import speech_input as si
import numpy as np
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


print value
me = np.mean(value) 	
print "The mean value is"
print me
print "The standard Deviation is "
stand = np.std(value)
print stand
cons_value = value - me
print ("the noise free value is %",cons_value)
min = np.min(value)
print min
print "Saved the feature vector fot RNN"