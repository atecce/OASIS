#!/usr/bin/env python

# need this for command line arguments
import sys

# need this for REST API
from REST import REST

# need this for sorted dictionary
import collections

# need this for moving average
import numpy as np

# need this to chain SysIDs
from itertools import chain

# set up REST backend 
firebase = REST()

# chain temperature SysIDs
SysIDs = chain(range(103, 104), range(201, 204))

def main(argv):

	# factor which determines sparseness
	N = int(argv[1])

	# for each temperature sensor
	for SysID in SysIDs:

		# hacky, accounts for different subsystems
		if SysID == 103:

			# declare table
			table = "data/sensors/liquid_tanks_and_plumbing/S" + str(SysID) + ".json"

		elif SysID in range(201, 204):

			# declare table
			table = "data/sensors/growth_medium/S" + str(SysID) + ".json"

		# get data
		data = firebase.GET(table)

		# clean data
		cleaned = {int(k): v for k, v in data.items() if v >= 0}

		# sort data by key
		cleaned = collections.OrderedDict(sorted(cleaned.items()))

		epochs   = cleaned.keys()
		readings = cleaned.values()

		# smooth data
		smoothed_epochs   = np.convolve(epochs,   np.ones((N,))/N, mode = 'valid')
		smoothed_readings = np.convolve(readings, np.ones((N,))/N, mode = 'valid')

		smoothed = dict(zip(smoothed_epochs, smoothed_readings))

		# make sparse
		sparse = dict()

		count = int()

		for key in smoothed:

			if count % N == 0:

				sparse[key] = smoothed[key]

			count += 1

		# convert float keys to integers
		sparse = {int(k): v for k, v in sparse.items()}

		# post data
		firebase.PUT(sparse, table)

if __name__ == "__main__": main(sys.argv)
