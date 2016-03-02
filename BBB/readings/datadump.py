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

# SysID's for sensors being read not
SysIDs = chain(range(101, 104), range(201, 204), range(301, 303), range(304, 306))

# iterate through SysID's
for SysID in SysIDs: 

	# read from the csv file
	with open('S'+str(SysID)+'.csv') as csvfile:

		# set table name
		table = 'S'+str(SysID)+'.json'

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

				entry = {fourth: float(reading[2])}

				print table, json.dumps(entry)

			# originally introduced for failed entry in pH
			except ValueError: continue
