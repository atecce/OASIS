# need this for log and exponent
import math

# need this for OrderedDict
import collections

# need this to get data
from REST import REST

# best estimate of ambient parts per million
PPM_a = 450

# solve for the constant in exponential decay
def constant(delta_PPM, delta_t):

	return math.log(delta_PPM) / delta_t

# model of parts-per-million over time
def model(k, t, PPM_a):

	return math.exp(k*t) + PPM_a

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

# separate keys and values
epochs   = CO2data.keys()
readings = CO2data.values()

# initialize list of indices where there are gaps in the readings
reading_gaps = list()

for i in range(1, len(readings)): 

	# set CO2 threshold at 50 parts per-million	
	if readings[i]-readings[i-1] > .005: 

		print epochs[i-1], epochs[i]
		print readings[i-1], readings[i]

		# append index 
		reading_gaps.append(i)

print reading_gaps
