# need this to get random values
import random

class test_sensor:

	""" This is a random normal variable which will cross both sides of the HSST's.
	    The main test is to see whether the appropriate actuators are toggled when
	    the thresholds are crossed. For more information on how this works, see:
	    https://en.wikipedia.org/wiki/Normal_distribution """

	def __init__(self, HSST_low, HSST_high):

		# set HSST's
		self.HSST  = {"low": HSST_low, "high": HSST_high}

		# these are picked such that the value is virtually guaranteed to cross both HSST thresholds
		self.mu    = (self.HSST["high"] + self.HSST["low"]) / 2
		self.sigma = (self.HSST["high"] - self.HSST["low"]) / 2

	def read(self):

		# returns the random value
		return random.gauss(self.mu, self.sigma)

	def read_low(self):

		# returns a value two standard deviations below the mean
		return self.HSST["low"] - 2*self.sigma

	def read_high(self):

		# returns a value two standard deviations above the mean
		return self.HSST["high"] + 2*self.sigma

# set up all sensors
EC         = test_sensor(1150, 1250)
pH         = test_sensor(5.5, 6)
day_temp   = test_sensor(23, 27)
night_temp = test_sensor(18, 22)
soil_temp  = test_sensor(15, 20)
water_temp = test_sensor(22, 24)
humidity   = test_sensor(50, 70)
pressure   = test_sensor(80, 84)
CO2        = test_sensor(1000, 2000)
PAR        = test_sensor(200, 250)

# this is a list of observations indexed t = 0, 1, 2, ...
O = list()

# length of time steps
T = int(1000)

# this for loop creates a simulated time series for the specified time T
for t in range(T):

	# observe
	observation = (EC.read(), 	  pH.read(), 	   day_temp.read(), night_temp.read(), soil_temp.read(),  \
                       water_temp.read(), humidity.read(), pressure.read(), CO2.read(),        PAR.read())

	# store
	O.append(observation)

	print observation
