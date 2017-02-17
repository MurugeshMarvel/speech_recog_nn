import numpy as np
import scipy.signal as scisig

class lpc(object):
	
	def stackOLA(self,input_ola,window_ola):
		input_len = np.len(input_ola)
		new_window_ola_len = np.len(window_ola)
		step_stack = int(new_window_func*0.5)
		count_stack = int((input_len-new_window_ola_len)/step_stack) + 1
		ola_stack = np.zeros((new_window_ola_len, count_stack))
		for i in range(0,count_stack):
			ola_stack[i]=window_ola*input_ola[1:new_window_ola_len + ((i-1)*step)] #have to correct the array format

		return ola_stack

	def pressStake(self,press_input):
		new_window_press,count_press = np.size(press_input)
		step_press = int(new_window_press*0.5)
		n = (count_press-1) * step_press + new_window_press
		press_ip = np.zeros(n,1)
		for i in range(0,count_press):
			press_ip =

		return press_ip

	def lpc_main(self,input_lpc,filter_order):
		N = len(input_lpc)
		b = input_lpc[1:N]
		input_lpc_z = np.array([[input_lpc],[np.zeros(filter_order,1)]])
		A = np.zeros(N-1,filter_order)
		for i in range(0,filter_order):
			temp = np.roll(input_lpc_z,i-1)
			A[:,i] = temp[1:(N-1)]
		coeff_lpc = A/b
		#calculating Variance of errors
		errors_lpc = b - (A*coeff_lpc)
		variance_lpc = np.var(errors_lpc)
		return coeff_lpc,variance_lpc,errors_lpc
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
				decode_op[i] = window_decode * filter

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
					step_decode = round(1/pitch_frequency[i])
					pts = range((offset+1),new_window_decode_2,step_decode)
					if pts:
						pts_len = len(pts)
						offset = step_decode + pts[pts_len] - new_window_decode_2
						src_decode[pts] = np.sqrt(step_decode)

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
			b,a = scisig.utter(10,lowcut, 'high')#have to compute this
			decode_op = scisig.lfilter(b,a,decode_op)#have to compute this

		


		return decode_op





if __name__ == '__main__':
	lpc_object = lpc()
	lpc.encode()
