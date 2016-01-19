#!/usr/bin/env python

# need this to thread
import threading

# need this to delay
import time

class myThread(threading.Thread):

	def __init__(self, threadID, name, counter):

		# call parent constructor to retain thread behavior
		threading.Thread.__init__(self)

		# set attributes
		self.threadID = threadID	# id
		self.name     = name		# name
		self.counter  = counter		# counter

	def run(self):

		# run print time
		print "Starting " + self.name
		print_time(self.name, self.counter, 5)
		print "Exiting " + self.name

def print_time(threadName, delay, counter):

	# while counter is greater than zero
	while counter:

		# wait for the delay
		time.sleep(delay)

		# print thread info
		print "%s: %s" % (threadName, time.ctime(time.time()))

		# decrement counter
		counter -= 1

# create threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# start threads
thread1.start()
thread2.start()

# notify exit
print "Exiting Main Thread"
