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

# split dictionary into two lists
epochs   = CO2data.keys()
readings = CO2data.values()

# initialize segments with reading gaps
segments = list()

# first list of segment
segments.append(list())

# index of segments
segment_index = int()

# for each reading
for index in range(1, len(readings)):

	# threshold for gap in readings at 50 ppm
	if readings[index] - readings[index-1] > .005: 

		# increment segments
		segments.append(list())
		segment_index += 1

	# add index of reading to most recent segment
	segments[segment_index].append(index)

# index csv's starting at 1
for index in range(1, len(segments)+1):

	# write data to csv
	with open("CO2_" + str(index)+ ".csv", 'w') as datafile:

		# write headers
		datafile.write("epoch, reading, ,epoch, ln(reading)\n")

		# write each entry
		for entry in segments[index-1]: 
			
			datafile.write(str(epochs[entry]-epochs[segments[index-1][0]])+', ' + str(readings[entry])+',,')
			datafile.write(str(epochs[entry]-epochs[segments[index-1][0]])+', ' + str(math.log(readings[entry]))+'\n')
