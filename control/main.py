# need this for sensors
from sensors import sensor_suite

# need this to connect with database
from networking import 

# start counter for time step
time = int()

# declare different possible states 
states = {"initiating", "germinate", "autopilot", "standby", "shutdown"}

# initialize state
state mode = initiating;

# string for now, this is rather open-ended
choice = str()

def sense():

	# thread this process for the duration of the program
	while True:

		# initialize observation
		observation = list()
		
		# for each sensor, record the observation
		for sensor in sensor_suite: observation.append(sensor.read())

		# send observation to server
		dump(observation)

def act(): 

	# toggle each actuator
	for (int i = 0; i < actuator_amt; i++) actuator_suite[i].toggle();

def obey(choice)

	# map the components to a list of natural numbers 0, 1, ..., sensor_amt + actuator_amt
	if   choice == 0: pass
	elif choice == 1: pass 
	       .
	       .
	       .
        elif choice == sensor_amt + actuator_amt - 1: pass

# should start at system start up
initiate()

# sense as often as possible. the more data, the better, whether you're going to use it or not
# need python replacement
thread consciousness (sense)

# signals from user, presumably
while mode != shutdown:

	# decide what to do next based on what mode you are in
	if   mode == "germinate": germinate()
	elif mode == "autopilot": act()

	elif standby:

		choice = prompt()
		obey(choice)

	elif shutdown: break

	else: userInputError()

	# increment time step
	time += 1

# need python replacement
system("shutdown -P now");
