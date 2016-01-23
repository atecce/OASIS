#!/usr/bin/env python

# need this to generate plausible benchmark
import random

# need this for unit tests class
import unittest

from statistics import statistics

class statistics_test(unittest.TestCase):

	n = int(10000)

	def test_standard_uniform_distribution(self):

		sample = list()

		for i in range(self.n): sample.append(random.random())

		standard_uniform = statistics(sample)

		print
		print "test of standard uniform distribution"
		print
		print "\tsample size:", self.n
		print
		print "\tsample mean:", standard_uniform.mu
		print "\texpectation:", float(1) / float(2)
		print
		print "\tsample variance:", standard_uniform.sigma_squared
		print "\tvariance:", float(1) / float(12)
		print

	def test_standard_normal(self):

		sample = list()

		for i in range(self.n): sample.append(random.gauss(0, 1))

		standard_normal = statistics(sample)

		print
		print "test of standard normal distribution"
		print
		print "\tsample size:", self.n
		print
		print "\tsample mean:", standard_normal.mu
		print "\texpectation:", 0
		print
		print "\tsample variance:", standard_normal.sigma_squared
		print "\tvariance:", 1
		print

if __name__ == "__main__": unittest.main()
