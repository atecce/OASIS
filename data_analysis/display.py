# need this for command line arguments
import sys

# need this to convert epoch to datetime
import time

# need this to get data
from API.REST import REST

# need this to convert senseID to SysID
from API.conversions import senseIDtoSysID

# set up database
firebase = REST("https://cumarsoasis.firebaseio.com/")

def main(argv):

	# user input is sense ID
	senseID = argv[1]

	# convert to SysID
	SysID = senseIDtoSysID[senseID]

	# get data
	data = firebase.GET("sensors/historical/S" + str(SysID) + ".json")

	# write csv file
	with open(senseID + 'data.csv', 'w') as f:

		# for each sequential entry
		for entry in sorted(data):

			# convert epoch to datetime
			datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(entry)))

			# write to csv
			f.write(str(datetime) + ', ' + str(data[entry]) + '\n')

			# print output
			print datetime, data[entry]

if __name__ == "__main__": main(sys.argv)
