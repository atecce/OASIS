# need this to chain SysID's together
from itertools import chain

# need this to get senseID
from conversions import SysIDtosenseID

class sensor:

	def __init__(self, SysID):

		# set SysID as string for read call
		self.SysID = str(SysID)

		# set senseID
		self.senseID = SysIDtosenseID[SysID]

	def read(self):

		# open temp file corresponding to sensor stream
		with open('/tmp/S'+self.SysID) as sense_file:

			# split the string by characters and convert them all to floats
			return float(sense_file.read().rstrip())

# chain SysID's together
SysIDs = chain(range(101, 113), range(201, 204), range(205, 207), range(208, 212), range(301, 307), range(401, 404))

# initialize suite of sensors as dictionary
S = dict()

# create suite of sensors
for SysID in SysIDs: S[SysID] = sensor(SysID)
