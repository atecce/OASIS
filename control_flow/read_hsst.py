# open HSST file

# Read in Variables

# Check for new HSST every 60 seconds

import pandas as pd

class HSST:

	def __init__(self):

		self.hsst = pd.read_csv('HSST.csv')

	def read(self, row, col):
		
		return self.hsst[row][column]

