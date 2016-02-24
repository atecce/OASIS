#!usr/bin/env python

from firebase import firebase
firebase = firebase.FirebaseApplication('https://marsoasis.firebaseio.com', None)
while True:
	commands = firebase.get('/commands', None)
	if commands != None:
		for command in commands.keys():
			print "running " + str(command) + " on " + str(commands[command])
		firebase.delete('/commands', None)
		

