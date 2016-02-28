class sensor:

	def __init__(self, SysID):

		self.SysID = SysID

	def read(self):

		with open('tmp/S'+SysID) as sense_file:

			return float(sense_file.read())
