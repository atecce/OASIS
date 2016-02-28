# need this to get random values
import random

# need this to wait
import time

# need this for current time
import datetime

class test_sensor:

	""" This is a random normal variable which will cross both sides of the HSST's.
	    The main test is to see whether the appropriate actuators are toggled when
	    the thresholds are crossed. For more information on how this works, see:
	    https://en.wikipedia.org/wiki/Normal_distribution """

	def __init__(self, table, HSST_low, HSST_high):

		# table name
		self.table = table

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

class test_RHTemp:

	""" This is a special case because multiple values are returned and because 
	    the HSST's vary based on time of day. """

	# table name
	table = "rh_and_air_temp"

	# humidity
	humidity_HSST = {"low": 50, "high": 70}

	humidity_mu    = (humidity_HSST["high"] + humidity_HSST["low"]) / 2
	humidity_sigma = (humidity_HSST["high"] - humidity_HSST["low"]) / 2

	# air temperature during the day
	air_temp_day_HSST = {"low": 23, "high": 27}

	air_temp_day_mu    = (air_temp_day_HSST["high"] + air_temp_day_HSST["low"]) / 2
	air_temp_day_sigma = (air_temp_day_HSST["high"] - air_temp_day_HSST["low"]) / 2

	# air temperature during the night
	air_temp_night_HSST = {"low": 18, "high": 22}

	air_temp_night_mu    = (air_temp_night_HSST["high"] + air_temp_night_HSST["low"]) / 2
	air_temp_night_sigma = (air_temp_night_HSST["high"] - air_temp_night_HSST["low"]) / 2

	def read(self):

		# daytime here is defined as anytime between 6 AM and 6 PM
		# this is Earth time, the rotational period of Mars is 24 hours and 30 minutes, so it's actually not too bad an approximation
		day = (6 <= datetime.datetime.now().hour <= 18)

		# conditional on the time of day
		if day: return random.gauss(self.air_temp_day_mu,   self.air_temp_day_sigma),   random.gauss(self.humidity_mu, self.humidity_sigma)
		else:   return random.gauss(self.air_temp_night_mu, self.air_temp_night_sigma), random.gauss(self.humidity_mu, self.humidity_sigma)

	def read_low(self):

		# daytime here is defined as anytime between 6 AM and 6 PM
		# this is Earth time, the rotational period of Mars is 24 hours and 30 minutes, so it's actually not too bad an approximation
		day = (6 <= datetime.datetime.now().hour <= 18)

		# conditional on the time of day
		if day: return self.air_temp_day_HSST["low"]   - self.air_temp_day_sigma,   self.humidity_HSST["low"] - self.humidity_sigma
		else:   return self.air_temp_night_HSST["low"] - self.air_temp_night_sigma, self.humidity_HSST["low"] - self.humidity_sigma

	def read_high(self):

		# daytime here is defined as anytime between 6 AM and 6 PM
		# this is Earth time, the rotational period of Mars is 24 hours and 30 minutes, so it's actually not too bad an approximation
		day = (6 <= datetime.datetime.now().hour <= 18)

		# conditional on the time of day
		if day: return self.air_temp_day_HSST["high"]   + self.air_temp_day_sigma,   self.humidity_HSST["high"] + self.humidity_sigma
		else:   return self.air_temp_night_HSST["high"] + self.air_temp_night_sigma, self.humidity_HSST["high"] + self.humidity_sigma

class test_actuator:

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
