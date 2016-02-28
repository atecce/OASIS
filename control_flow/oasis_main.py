#!usr/bin/env python

import logging # collect information about the program
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from read_hsst           import HSST           # system information that is subject to change frequently
from db_util             import FirebaseThread # thread to check for new info from the firebase db
from germinate           import * # have to figure out what we need to import from all these
from mixing              import *
from system_health_check import initial_health_check
from system_shutdown     import shutdown
from datetime            import datetime

class OASIS:
	'''
	Semi-autonomous control system for LabOASIS
	'''
	# automatically startup a thread to continuously check for new commands and new data
	incoming = FirebaseThread()

	# collect all the information from the HSST
	hsst = HSST()

	def __init__(self, time):
		self.startup_time = time

	def run(self, mode):
		if mode == 'initiating':
			# check to make sure everything is functioning properly
			if not initial_health_check(): # something is wrong
				shutdown()
				# log info here

			# even though we already have a thread set up
			# for getting information (data, commands)
			# from the database, we still have to write
			# "continuous_monitor_and_record" to make sense of
			# all that information. my first thought is to
			# handle all of that in the db_util FirebaseThread,
			# but there are certainly other solutions

def main():
	# construct the system class
	oasis = OASIS(str(datetime.now()))

	# fire up the system
	oasis.run('initiating')

if __name__=='__main__': main()
