import numpy as np

class lpc(object):
	def encode(input_sig,order,window):
		signal = stackOLA(input_sig,window)
		new_window, n = size(signal)
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




if __name__ == '__main__':
	lpc_object = lpc()
	lpc.encode()
