# need this for datetime
import datetime

# need this to strip last character
import os

# need this for json file
import json

# need this to parse csv's
import csv

# need this to chain SysID's
from itertools import chain

# need this to use firebase
import firebase

sensor_conversion = {"401": "relative humidity and air temperature", "402": "total pressure", "403": "photosynthetically active radiation", "301": "relative humidity and air temperature", "302": "relative humidity and air temperature", "303": "total pressure", "304": "oxygen", "305": "carbon dioxide", "306": "photosynthetically active radiation", "201": "soil temperature", "202": "soil temperature", "203": "soil temperature", "205": "electrical conductivity", "206": "pH", "208": "moisture", "209": "moisture", "210": "moisture", "211": "moisture", "101": "electrical conductivity", "102": "pH", "103": "liquid temperature", "104": "dissolved oxygen", "105": "liquid level", "106": "liquid level", "107": "liquid level", "108": "liquid level", "109": "liquid level", "110": "flow meter", "111": "flow meter", "112": "liquid level"}

# SysID's for sensors being read not
SysIDs = chain(range(101, 104), range(201, 204), range(301, 303), range(304, 306))

# iterate through SysID's
for SysID in SysIDs: 

	# get sensor type from conversion table
	sensor_type = sensor_conversion[str(SysID)]

	# initialize x axis with date time
	x = list()

	# initialize y axis with sensor type
	y = list()

	# read from the csv file
	with open('S'+str(SysID)+'.csv') as csvfile:

		# take in all the readings
		readings = csv.reader(csvfile)

		# for each reading
		for reading in readings: 

			try: 

				# get datetime in one string
				datetime_format = str(reading[0])+str(reading[1])

				# split the string by space
				first = datetime_format.split()

				# split date by hyphen, split time by colon
				second = first[0].split('-') + first[1].split(':')

				# convert strings to integers
				third = map(int, second)

				# convert to epoch
				fourth = datetime.datetime(third[0], third[1], third[2], third[3], third[4], third[5]).strftime('%s')

				# append date time
				x.append(int(fourth))

				# append reading
				y.append(float(reading[2]))

			# originally introduced for failed entry in pH
			except ValueError: continue

	# put readings in json format
	sensor_readings = {"epoch": x, sensor_type: y}

	# dump results to JSON file
	with open('S'+str(SysID)+'.json', 'w') as jsonfile: json.dump(sensor_readings, jsonfile)
