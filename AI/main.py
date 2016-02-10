# need this for sensors
from sensors import sensor_suite

# need this to connect with database
from networking import * #imports load, dump, dump_to_db

# need this function to get the current time
from time import localtime

# declare different possible states 
states = {"initiating", "germinate", "autopilot", "standby", "shutdown"}

# initialize state
mode = "initiating"

# string for now, this is rather open-ended
choice = str()

# how often to send information to the database
observation_frequency = 15

def sense():

	# thread this process for the duration of the program
	while True:

		# observe
		observation = [sensor.read() for sensor in sensor_suite]

		# send 
		dump(observation)
		
		# write to db
		map(dump_to_db, [sensor.table, sensor.name, sensor.read() for sensor in sensor_suite])

def act(): 

	# toggle each actuator
	for actuator in actuator_suite: actuator[i].toggle();

def obey(choice)

	# map the components to a list of natural numbers 0, 1, ..., len(sensor_suite) + len(actuator_suite) - 1
	if   choice == 0: pass
	elif choice == 1: pass 
	       .
	       .
	       .
        elif choice == len(sensor_suite) + len(actuator_suite) - 1: pass

def run(mode):
	# signals from user
	while mode != "shutdown":

		# chris seemed to think that threading wouldn't be the best option for sensor data collection
		# here is another idea i had
		# localtime() returns a struct with the current time
		# the 4th index contains the current minute (0-60)
		# so if observation_frequency is 15, the program will sense at 15 minute intervals
		if   localtime()[4] % observation_frequency == 0: sense() 
	
		# plant the seeds
		if   mode == "germinate": germinate()
	
		# activate AI
		elif mode == "autopilot": act()
	
		# command prompt interface
		elif standby:
	
			choice = prompt()
			obey(choice)

		# shutdown
		elif shutdown: break

		# throw error
		else: userInputError()

# should start at system start up
initiate()

# might abandon threading
# sense as often as possible. the more data, the better, whether you're going to use it or not
# need python replacement
thread consciousness (sense)

# try to run the program indefinitely
try:
	
	run(mode)

# catch interrupt
except KeyboardInterrupt:

	mode = raw_input("Enter new runmode: ")
	# startup again (or shutdown)
	run(mode) # this code will not work, because it only allows for one interruption. going to have to find a different solution 

finally:
	
	# need python replacement
	system("shutdown -P now");
