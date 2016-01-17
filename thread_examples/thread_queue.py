#!/usr/bin/env python

# need this for queue
import Queue

# need this for threads
import threading

# need this for delay
import time

# initalize exit flag
exitFlag = int()

class myThread(threading.Thread):

	def __init__(self, threadID, name, q):

		# call parent constructor to retain thread behavior
		threading.Thread.__init__(self)

		# set attributes
		self.threadID = threadID	# id
		self.name     = name		# name
		self.q        = q		# queue

	def run(self):

		# process data
		print "Starting " + self.name
		process_data(self.name, self.q)
		print "Exiting " + self.name

def process_data(threadName, q):

	# while the exit flag hasn't been changed
	while not exitFlag:

		queueLock.acquire()

		if not workQueue.empty():

			data = q.get()
			queueLock.release()
			print "%s processing %s" %(threadName, data)

		else:

			queueLock.release()

		time.sleep(1)

# initalize thread list
threadList = ["Thread-1", "Thread-2", "Thread-3"]

# initialize name list
nameList   = ["One", "Two", "Three", "Four", "Five"]

# initialize thread lock
queueLock = threading.Lock()

# initalize queue
workQueue = Queue.Queue(10)

# initalize list of threads
threads = list()

# initalize thread id
threadID = 1

# for each name in thread list
for tName in threadList:

	# construct thread
	thread = myThread(threadID, tName, workQueue)

	# start thread
	thread.start()

	# add it to the list
	threads.append(thread)

	# increment the thread id
	threadID += 1

# populate queue with words, one at a time
queueLock.acquire()
for word in nameList: workQueue.put(word)
queueLock.release()

# wait for empty queue
while not workQueue.empty(): pass

# switch exit flag
exitFlag = 1

# wait for all the threads
for t in threads: t.join()
print "Exiting Main Thread"
