# need this for sensors
from sensors import sensor_suite

# need this to connect with database
from networking import * #imports load, dump, dump_to_db

# declare different possible states 
states = {"initiating", "germinate", "autopilot", "standby", "shutdown"}

# initialize state
mode = "initiating"

# string for now, this is rather open-ended
choice = str()

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

# should start at system start up
initiate()

# sense as often as possible. the more data, the better, whether you're going to use it or not
# need python replacement
thread consciousness (sense)

# signals from user, presumably
while mode != shutdown:

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

# need python replacement
system("shutdown -P now");
