import unittest
from sensors import sensor_suite

class sensor_test(unittest.TestCase):

	def test_voltage(self):

		# sample size
		n = int(100)

		for sensor in sensor_suite:

			sample = list()

			# take a sample of size n
			for i in range(n): sample.append(sensor.read())

			for observation in sample:

				print sensor.name, sensor.sensor_range, sensor.read()

				self.assertTrue(sensor.sensor_range["low"] <= observation <= sensor.sensor_range["high"])

		# more pythonic way with 'for all observation in self.sample: sensor.sensor_range["low"] <= observation <= sensor.sensor_range["high"]'?

if __name__ == "__main__": unittest.main()
