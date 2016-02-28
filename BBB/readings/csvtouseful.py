# need this to strip last character
import os

# need this for json file
import json

# need this to parse csv's
import csv

# need this to chain SysID's
from itertools import chain

sensor_conversion = {"401": "relative humidity and air temperature", "402": "total pressure", "403": "photosynthetically active radiation", "301": "relative humidity and air temperature", "302": "relative humidity and air temperature", "303": "total pressure", "304": "oxygen", "305": "carbon dioxide", "306": "photosynthetically active radiation", "201": "soil temperature", "202": "soil temperature", "203": "soil temperature", "205": "electrical conductivity", "206": "pH", "208": "moisture", "209": "moisture", "210": "moisture", "211": "moisture", "101": "electrical conductivity", "102": "pH", "103": "liquid temperature", "104": "dissolved oxygen", "105": "liquid level", "106": "liquid level", "107": "liquid level", "108": "liquid level", "109": "liquid level", "110": "flow meter", "111": "flow meter", "112": "liquid level"}

# SysID's for sensors being read not
SysIDs = chain(range(101, 104), range(201, 204), range(301, 303), range(304, 306))

# open sql file
sqlfile = open('readings.sql', 'w')

# iterate through SysID's
for SysID in SysIDs: 

	# initialize x axis with date time
	x = ['date time']

	# initialize y axis with sensor type
	y = [sensor_conversion[str(SysID)]]

	# add insert statement to top of file
	sqlfile.write("insert into sensor_data (sensor_ID, read_at, reading) values\n")

	# read from the csv file
	with open('S'+str(SysID)+'.csv') as csvfile:

		# take in all the readings
		readings = csv.reader(csvfile)

		# for each reading
		for reading in readings: 

			try: 

				# append date time
				x.append(str(reading[0])+str(reading[1]))

				# append reading
				y.append(float(reading[2]))

				# write to file for 'insert into' statement
				sqlfile.write("\n\t("+str(SysID)+str(", '")+str(reading[0])+str(reading[1])+"', "+reading[2]+"),")

			# originally introduced for failed entry in pH
			except ValueError: continue

	# put readings in json format
	sensor_readings = {"columns":[x, y]}

	# dump results to JSON file
	with open('S'+str(SysID)+'.json', 'w') as jsonfile: json.dump(sensor_readings, jsonfile)

	# strip last comma
	sqlfile.seek(-1, os.SEEK_END)
	sqlfile.truncate()

	# end insert statement
	sqlfile.write(";\n\n")

# close the sql file
sqlfile.close()



