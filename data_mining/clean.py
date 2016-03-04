#!/usr/bin/env python

# need this for REST API
from REST import REST

# need this for sorted dictionary
import collections

# need this for moving average
import numpy as np

# set up REST backend 
firebase = REST()

# declare table
table = "/data/sensors/liquid_tanks_and_plumbing/S103.json"

# get data
data = firebase.GET(table)

# convert json keys to integers
data = {int(k): v for k, v in data.items()}

# clean data
cleaned = {k: v for k, v in data.items() if v >= 0}

# sort data by key
cleaned = collections.OrderedDict(sorted(cleaned.items()))

epochs   = cleaned.keys()
readings = cleaned.values()

# smooth data
smoothed_epochs   = np.convolve(epochs,   np.ones((10,))/10, mode = 'valid')
smoothed_readings = np.convolve(readings, np.ones((10,))/10, mode = 'valid')

smoothed = dict(zip(smoothed_epochs, smoothed_readings))

# make sparse by only keeping 1 in every 10 entries
sparse = dict()

count = int()

for key in smoothed:

	if count % 10 == 0:

		sparse[key] = smoothed[key]

	count += 1

# convert float keys to integers
sparse = {int(k): v for k, v in sparse.items()}

# post data
firebase.PUT(sparse, table)
