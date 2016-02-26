# Outline of the Control Procedure Code

# System power initiated

states = {"initiating", "germinate", "autopilot", "standby", "shutdown"}

# SET System mode to INITIATING

mode = "initiating"
 if mode == "initiating":
 	# RUN SYSTEM Health Checks
 	#set all actuators to off/0 and check that all sensors work
 	system_health_checks()
 	# RUN Monitor and Record
 	#start recording from sensors
	monitor_record()
	# RUN Read HSST
	#record all values from the HSST file
	read_HSST()

mode = "germinate"
if mode == "germinate":
	pass

while mode == "autopilot":
	#run autopilot.py






<<<<<<< Updated upstream
# RUN Read HSST
hsst = HSST()
print hsst.read('I', 28)
=======
>>>>>>> Stashed changes
