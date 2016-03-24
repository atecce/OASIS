# need this to convert epoch to datetime
import time

# need this to get data
from REST import REST

# set up database
firebase = REST("https://cumarsoasis.firebaseio.com/")

# get data
CO2data = firebase.GET("sensors/historical/S305.json")

# write csv file
with open('CO2data.csv', 'w') as f:

	# for each sequential entry
	for entry in sorted(CO2data):

		# convert epoch to datetime
		datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(entry)))

		# write to csv
		f.write(str(datetime) + ', ' + str(CO2data[entry]) + '\n')

		# print output
		print datetime, CO2data[entry]
