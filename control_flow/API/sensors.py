# need this to chain SysID's together
from itertools import chain

class sensor:

	def __init__(self, SysID):

		# identify sensor by SysID
		self.SysID = SysID

	def read(self):

		# open temp file corresponding to sensor stream
		with open('tmp/S'+SysID) as sense_file:

			# return the contents as a float
			return float(sense_file.read())

# chain SysID's together
SysIDs = chain(range(101, 113), range(201, 204), range(205, 207), range(208, 212), range(301, 307), range(401, 404))

# initialize suite of sensors as dictionary
S = dict()

# create suite of sensors
for SysID in SysIDs: S[SysID] = sensor(SysID)
