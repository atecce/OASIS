#!usr/bin/env python


from firebase.firebase import FirebaseApplication, FirebaseAuthentication
import threading
import time
          
class FirebaseThread(object):

	authentication = FirebaseAuthentication('05fRJb4X7uQe8WGbrZh4SvTAG4vJ6WtEL8SGwckK', 'jared.jolton@gmail.com', True, True)
	firebase       = FirebaseApplication('https://marsoasis.firebaseio.com', authentication)

	def __init__(self, interval=5):
        
		self.interval = interval
        	thread        = threading.Thread(target=self.run, args=())
        	thread.daemon = True                            

        	thread.start()                                  

	def run(self):
		while True:
			commands = self.firebase.get('/commands/', None)
			if commands != None:
				print commands
			self.firebase.delete('/commands', None)
            		time.sleep(self.interval)
