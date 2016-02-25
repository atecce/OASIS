# open HSST file

# Read in Variables

# Check for new HSST every 60 seconds

import pandas as pd

class HSST:

	def __init__(self):

		self.hsst = pd.read_csv('HSST.csv', names=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X'])

	def read(self, col, row):
		
		return self.hsst[col][row-1]

