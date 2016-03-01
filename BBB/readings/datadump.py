# need this for datetime
import datetime

# need this to parse csv's
import csv

# need this for json format
import json

# need this to chain SysID's
from itertools import chain

# need this to post to database
from REST import REST

# set up database interface
firebase = REST()

# SysID's for sensors being read not
SysIDs = chain(range(101, 104), range(201, 204), range(301, 303), range(304, 306))

## set table name
#table = "data.json"
#
#data = {"sensors":
#
#		{
#			"liquid_tanks_and_plumbing": dict(),
#			"growth_medium":	     dict(),
#			"internal_atmosphere":	     dict(),
#			"external_environment":	     dict()
#		}
#	}

# iterate through SysID's
for SysID in SysIDs: 

	# prepend S to SysID
	extended_SysID = 'S'+str(SysID)

	# initialize subsystem
	subsystem = str()

	# choose subsystem
	if SysID in range(100, 200): subsystem = "liquid_tanks_and_plumbing/"
	if SysID in range(200, 300): subsystem = "growth_medium/"
	if SysID in range(300, 400): subsystem = "internal_atmosphere/"
	if SysID in range(400, 500): subsystem = "external_environment/"

	# set table
	table = "data/sensors/" + subsystem + extended_SysID + ".json"

	# initialize entry
	entry = dict()

	# read from the csv file
	with open(extended_SysID + '.csv') as csvfile:

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
				epoch = datetime.datetime(third[0], third[1], third[2], third[3], third[4], third[5]).strftime('%s')

				# create entry
				entry[epoch] = float(reading[2])

			# originally introduced for failed entry in pH
			except ValueError: continue

	# send entry to database
	firebase.PUT(entry, table)
