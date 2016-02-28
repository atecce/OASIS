# need this to strip last character
import os

# need this for json file
import json

# need this to parse csv's
import csv

# need this to chain SysID's
from itertools import chain

# SysID's for sensors being read not
SysIDs = chain(range(101, 104), range(201, 204), range(301, 303), range(304, 306))

# initialize dictionary of SysID's
sensor_readings = dict()

# open sql file
sqlfile = open('readings.sql', 'w')

# iterate through SysID's
for SysID in SysIDs: 

	# add insert statement to top of file
	sqlfile.write("insert into sensor_data (sensor_ID, read_at, reading) values\n")

	# initialize time indexed list of sensor readings for each SysID
	sensor_readings[SysID] = list()

	# read from the csv file
	with open('S'+str(SysID)+'.csv') as csvfile:

		# take in all the readings
		readings = csv.reader(csvfile)

		# for each reading
		for reading in readings: 

			try: 
			
				# date and time is key, reading is value
				entry = {str(reading[0])+str(reading[1]): float(reading[2])}

				# write to file for 'insert into' statement
				sqlfile.write("\n\t("+str(SysID)+str(", '")+str(reading[0])+str(reading[1])+"', "+reading[2]+"),")

			# originally introduced for failed entry in pH
			except ValueError: continue

			# append entry to list
			sensor_readings[SysID].append(entry)

	# strip last comma
	sqlfile.seek(-1, os.SEEK_END)
	sqlfile.truncate()

	# end insert statement
	sqlfile.write(";\n\n")

# close the sql file
sqlfile.close()

# dump results to JSON file
with open('S.json', 'w') as jsonfile: json.dump(sensor_readings, jsonfile)
