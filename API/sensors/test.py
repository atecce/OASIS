#!/usr/bin/env python

# need this for unit tests
import unittest

# import the suite of sensors
from sensors import sensor_suite

class sensor_test(unittest.TestCase):

#	def test_ranges(self):
#
#		# sample size
#		n = int(1)
#
#		# for each sensor
#		for sensor in sensor_suite:
#
#			# initalize sample
#			sample = list()
#
#			# take a sample of size n
#			for i in range(n): sample.append(sensor.read())
#
#			# for each observation
#			for observation in sample:
#
#				# print the results
#				print sensor.name, sensor.sensor_range, sensor.read()
#
#				# check if observation lies in sensor range
#				self.assertTrue(sensor.sensor_range["low"] <= observation <= sensor.sensor_range["high"])
#
#		# more pythonic way with 'for all observation in self.sample: sensor.sensor_range["low"] <= observation <= sensor.sensor_range["high"]'?

	def test_sample_sensors(self):

		# sample size
		n = int(100)

		# for each sensor
		for sensor in sensor_suite:

			# if a connection has been made
			if sensor.connection: 

				# initalize sample
				sample = list()

				# take a sample of size n
				for i in range(n): sample.append(sensor.read())

				mean_hat = sum(sample) / n

				variance_hat = float()

				for x in sample: variance_hat += (x - mean_hat)**2

				variance_hat = float(1) / float(n-1)

				print
				print "sensor:", sensor.name
				print "expected range:", sensor.sensor_range["low"], sensor.sensor_range["high"]
				print "actual range:", min(sample), max(sample)
				print "mean:",   mean_hat
				print "variance:", variance_hat
				print

if __name__ == "__main__": unittest.main()
