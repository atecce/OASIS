#!/usr/bin/env python

# need this for unit tests
import unittest

# need this for thread tests
import time

# import the suite of sensors
from sensors import sensor_suite

class sensor_test(unittest.TestCase):

	def test_ranges(self):

		# sample size
		n = int(1)

		# for each sensor
		for sensor in sensor_suite:

			# initalize sample
			sample = list()

			# take a sample of size n
			for i in range(n): sample.append(sensor.read())

			# for each observation
			for observation in sample:

				# print the results
				print sensor.name, sensor.sensor_range, sensor.read(), sensor.units

				# check if observation lies in sensor range
				self.assertTrue(sensor.sensor_range["low"] <= observation <= sensor.sensor_range["high"])

		# more pythonic way with 'for all observation in self.sample: sensor.sensor_range["low"] <= observation <= sensor.sensor_range["high"]'?

	def test_observations(self):

		# initialize length of time (in cycles)
		T = int(100)

		# initalize list of observations
		O = list()

		for t in range(T):

			# initalize entry
			entry = dict()

			# for each sensor, add it's reading
			for sensor in sensor_suite: entry[sensor.name] = sensor.read()

			print t, entry

			# append entry to list of observations
			O.append(entry)

if __name__ == "__main__": unittest.main()
