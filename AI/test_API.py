# need this to get random values
import random

# need this to wait
import time

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
		return self.HSST["low"] - self.sigma

	def read_high(self):

		# returns a value two standard deviations above the mean
		return self.HSST["high"] + self.sigma

class test_air_temperature:

	""" This is a special case because the HSST's for temperature vary from day to
	    to night and from air to soil and water (need to consult with Noah, on which
	    is which, assuming day and night only are concerns for air for now). """

	# daytime
	day_HSST   = {"low": 23, "high": 27}

	day_mu    = (day_HSST["high"] + day_HSST["low"]) / 2
	day_sigma = (day_HSST["high"] - day_HSST["low"]) / 2

	# nighttime
	night_HSST = {"low": 18, "high": 22}

	night_mu    = (night_HSST["high"] + night_HSST["low"]) / 2
	night_sigma = (night_HSST["high"] - night_HSST["low"]) / 2

	def read(self):

		# this is pseudo-code
		if   time is day:   return random.gauss(self.day_mu,   self.day_sigma)
		elif time is night: return random.gauss(self.night_mu, self.night_sigma)

	def read_low(self):

		# returns a value two standard deviations below the mean
		if   time is day:   return self.day_HSST["low"]   - self.day_sigma
		elif time is night: return self.night_HSST["low"] - self.night_sigma 

	def read_high(self):

		# returns a value two standard deviations above the mean
		if   time is day:   return self.day_HSST["high"]   + self.sigma
		elif time is night: return self.night_HSST["high"] + self.sigma

# set up all sensors
day_temp   = test_sensor(23, 27)
night_temp = test_sensor(18, 22)
soil_temp  = test_sensor(15, 20)
water_temp = test_sensor(22, 24)
humidity   = test_sensor(50, 70)
pressure   = test_sensor(80, 84)
CO2        = test_sensor(1000, 2000)
PAR        = test_sensor(200, 250)

EC = {1: test_sensor(1150, 1250),
      2: test_sensor(1150, 1250)}

pH = {1: test_sensor(5.5, 6),
      2: test_sensor(5.5, 6)}

class actuator:

	def __init__(self, name):

		# assign name 
		self.name = name

		# all actuators start as "off"
		self.status = "off"

	def check_status(self): 

		return self.status

	def toggle(self):

		if   self.status == "on":  self.status = "off"
		elif self.status == "off": self.status = "on"

# set up all the actuators
actuator_suite = list()

# one heater
actuator_suite.append(actuator("heater"))

# one chiller
actuator_suite.append(actuator("chiller"))

# one O2 concentrator
actuator_suite.append(actuator("O2 concentrator"))

# twelve pumps
pump = {1:  actuator("Pump 1"),
	2:  actuator("Pump 2"),
	3:  actuator("Pump 3"),
	4:  actuator("Pump 4"),
	5:  actuator("Pump 5"),
	6:  actuator("Pump 6"),
	7:  actuator("Pump 7"),
	8:  actuator("Pump 8"),
	9:  actuator("Pump 9"),
	10: actuator("Pump 10"),
	11: actuator("Pump 11"),
	12: actuator("Pump 12")}

for i in range(1, 13): actuator_suite.append(pump[i])

# two fans
fan = {1: actuator("Fan 1"),
       2: actuator("Fan 2")}

for i in (1, 2): actuator_suite.append(fan[i])

# overhead light
actuator_suite.append(actuator("Overhead light"))
