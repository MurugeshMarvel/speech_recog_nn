import numpy as np

class lpc(object):
	
	def stackOLA(self,input_ola,window_ola):
		input_len = np.len(input_ola)
		new_window_ola_len = np.len(window_ola)
		step = int(new_window_func*0.5)
		count = int((input_len-new_window_ola_len)/step) + 1
		ola_stack = np.zeros((new_window_ola_len, count))
		for i in range(0,count):
			ola_stack[i]=window_ola*input_ola[1:new_window_ola_len + ((i-1)*step)] #have to correct the array format

		return ola_stack

	def encode(self,input_sig,order,window):
		signal = stackOLA(input_sig,window)
		new_window, n_encode = size(signal)
		##lpc encode
		coeff = np.zeros((order, n))
		sig_power = np.zeros((1,n))
		error_sig = np.zeros((new_window,n))
		for i in range(0:n):
			new_coeff, new_sig_power, new_error_sig = myplc(signal[i],order)
			coeff[i] = new_coeff
			sig_power[i] = new_sig_power
			error_sig[2:new_window] = new_error_sig[i]
		return coeff, sig_power,error_sig


	def decode(self,filter_coeff,sig_power_fundfreq,window_decode,lowcut=0):
		ne,n_decode = np.size(sig_power_fundfreq)
		new_window_decode = len(window_decode)
		'''Synthesizing estimates for each chunks'''
		decode_op = np.zeros(new_window_decode,n_decode)
		if ne < 2:
			for i in range(0,n):
				src_decode = np.random.random(new_window_decode)
				decode_op[i] = ##have to solve the correct array structure in octave

		elif ne < 3:
			pitch_frequency = sig_power_fundfreq[1][:]
			power = sig_power_fundfreq[0][:]
			offset = 0
			new_window_decode_2 = round(new_window_decode/2)
			decode_op = np.zeros(new_window_decode_2*n,1)

			for i in range(0,n):
				#creating source
				if pitch_frequency[i] > 0:
					src_decode = np.zeros(new_window_decode_2,1)
					step = round(1/pitch_frequency[i])
					pts = range((offset+1),new_window_decode_2,step)
					if pts:
						pts_len = len(pts)
						offset = step + pts[pts_len] - new_window_decode_2
						src_decode[pts] = np.sqrt(step)

				else:
					src_decode = np.random.random(new_window_decode_2)
					offset = 0
				#filter
				decode_op = ##have to  solve the correct array structure in octave
		else:
			for i in range(0:n_decode):
				decode_op = ##have to solve the correct array structure in octave
				decode_op = pressStack(decode_op)

		if lowcut > 0 :
			b,a = butter(10,lowcut, 'high')#have to compute this
			decode_op = filter(b,a,decode_op)#have to compute this

		


		return decode_op





if __name__ == '__main__':
	lpc_object = lpc()
	lpc.encode()
