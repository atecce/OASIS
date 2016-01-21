#!/usr/bin/env python

# need this for unit tests
import unittest

# import the suite of sensors
from sensors import sensor_suite

class sensor_test(unittest.TestCase):

	def test_sample_RH_temp(self):

		# sample size
		n = int(5)

		# for each sensor
		for sensor in sensor_suite:

			# if a pin is specified
			if sensor.pin: 

				# initalize sample
				sample = list()

				# take a sample of size n
				for i in range(n): sample.append(sensor.read())
				
				humidities, temperatures = zip(*sample)				

				# take the sample means
				humidities_hat = sum(humidities) / n
				temperatures_hat = sum(temperatures) / n

				# take the sample variance
				variance_humid_hat = float()
				variance_temp_hat  = float()

				for observation in humidities:   variance_humid_hat += (observation - humidities_hat)**2
				for observation in temperatures: variance_temp_hat  += (observation - temperatures_hat)**2

				variance_humid_hat = (float(1) / float(n-1)) * variance_humid_hat
				variance_temp_hat  = (float(1) / float(n-1)) * variance_temp_hat

				# display results
				print
				print "sensor:", sensor.name
				print "pin:", sensor.pin
				print "expected range:", sensor.sensor_range["low"], sensor.sensor_range["high"]
				print "actual temp range:", min(temperatures), max(temperatures)
				print "actual humid range:", min(humidities), max(humidities)
				print "temperature mean:", temperatures_hat
				print "humidities mean:", humidities_hat
				print "variance temp:",  variance_temp_hat
				print "variance humid:", variance_humid_hat
				print

if __name__ == "__main__": unittest.main()
