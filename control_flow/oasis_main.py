#!usr/bin/env python

from read_hsst import HSST           # system information that is subject to change frequently
from db_util   import FirebaseThread # thread to check for new info from the firebase db

def main():
	
	incoming_data = FirebaseThread()
	print "waiting for data..."
	while True:
		pass

if __name__=='__main__': main()
