# need this to parse csv's
import csv

# need this to chain SysID's
from itertools import chain

# SysID's for sensors being read not
SysIDs = chain(range(101, 104), range(201, 204), range(301, 303), range(304, 306))

# initialize dictionary of SysID's
sensor_readings = dict()

# iterate through SysID's
for SysID in SysIDs: 
	
	# initialize time indexed list of sensor readings for each SysID
	sensor_readings[SysID] = list()

	# open the csv file
	with open('S'+str(SysID)+".csv") as csvfile:

		# take in all the readings
		readings = csv.reader(csvfile)

		# for each reading
		for reading in readings: 
			
			# date and time is key, reading is value
			entry = {(reading[0], reading[1]): reading[2]}

			# append entry to list
			sensor_readings[SysID].append(entry)

# check dictionary 
print sensor_readings
