import scipy.stats as st
import numpy as np

class gmmhmm:
	def __init__(self,n_states):
		self.n_states = n_states
		self.random_state = np.random.RandomState(0)
		self.prior= self.normalize(self.random_state.rand(self.n_states, 1))
		self.A = self._stochasticize(self.random_state.rand(sel.n_states, self.n_states))
		self.mu = None
		self.covs = None
		self.n_dims = None

	def _forward(self, B):
		log_likelihood = 0.
		T = B.shape[1]
		alpha = np.zeros(B.shape)
		for t in range(T):
			if t == 0:
				alpha[:,t] = B[:,t] * self.prior.ravel()


			else:
				alpha[:, t] = B[:, t] * np.dot(self.A.T, alpha[:,t-1])

			alpha_sum = np.sum(alpha[:,t])
			alpha[:,t] /= alpha_sum
			log_likelihood = log_likelihood + np.log(alpha_sum)

		return log_likelihood, alpha

	def backward(self,B):
		T = B.shape()
		beta = np.zeros(B.shape)
		beta[:, -1] = np.ones(B.shape[0])
		for t in range(T - 1)[::-1]:
			beta[:, t] = np.dot(self.A, (B[:,t+1] * beta[:,t +1]))
			beta[:,t] /= np.sum(beta[:,t])

		return beta

	def _stata_likelihood(self,obs):
		obs = np.atleast_2d(obs)
		B = np.zeros((self.n_states,obs.shape[1]))
		for s in range(self.n_states):
			np.random.seed(self.random_state.randint(1))
			B[s,:] = st.multivariate_normal.pdf(obs)