# need this for log and exponent
import math

# need this for OrderedDict
import collections

# need this to get data
from REST import REST

# set up backend to get data
firebase = REST()

# path to CO2 data
CO2path = "data/sensors/internal_atmosphere/S305.json"

# get CO2 data
CO2data = firebase.GET(CO2path)

# convert epoch values to integers
CO2data = {int(k): v for k, v in CO2data.items()}

# need it to be ordered
CO2data = collections.OrderedDict(sorted(CO2data.items()))

# initialize list of time segments
segments = list()
segments.append(list())

segment_index = int()

last = int()

for epoch in CO2data:

	# special case for first entry
	if last == 0: last = epoch

	# set 30 seconds as threshold for sensor failure
	elif epoch-last > 30: 
		
		# add a new segment
		segments.append(list())
		segment_index += 1

		print epoch-last

	# append entry to current segment
	segments[segment_index].append(epoch)

	# set last entry
	last = epoch

# initialize list of lengths
lengths = list()

# initialize list of intervals
intervals = list()

# for each segment
for segment in segments:

	# set interval
	interval = segment[0], segment[-1]

	# append interval to list
	intervals.append(interval)

	# calculate length of segment
	length = segment[-1]-segment[0]

	# append length to list
	lengths.append(length)

# separate keys and values
epochs   = CO2data.keys()
readings = CO2data.values()

# write data to csv

with open("CO2.csv", 'w') as datafile:

	datafile.write("epochs, readings\n")

	for k in range(len(epochs)): 
		
		datafile.write(str(epochs[k])+', ' + str(readings[k]) + '\n')
