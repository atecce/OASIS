class statistics:

	def __init__(self, sample):

		self.sample        = sample
		self.n             = len(sample)
		self.mu            = self.sample_mean()
		self.sigma_squared = self.sample_variance()

	def sample_mean(self):

		return float(sum(self.sample)) / float(self.n)

	def sample_variance(self):

		variance = float()

		for observation in self.sample:

			deviation = observation - self.mu

			variance += deviation**2

		variance *= float(1) / float(self.n-1)

		return variance
