#!/usr/bin/env python

# need this for tests
import random

# need this for unit tests
import unittest

from statistics import statistics

class statistics_test(unittest.TestCase):

	def test_standard_uniform_distribution(self):

		sample = list()

		n = int(10000)

		for i in range(n): sample.append(random.random())

		standard_uniform = statistics(sample)

		print
		print "sample mean:", standard_uniform.mu
		print "expectation:", float(1) / float(2)
		print
		print "sample variance:", standard_uniform.sigma_squared
		print "variance:", float(1) / float(12)
		print

if __name__ == "__main__": unittest.main()
