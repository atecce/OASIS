from API.test_actuators import F, V, M, P
from API.test_sensors import S


# Read [Health Sensors: voltage]

# IF health data meets conditions
# THEN set system mode to STANDBY
# THEN END

# ELSE RUN System Shutdown


#turn off all actuators
for actuator in actuator_suite:
	actuator[i].toggle()
	actuator[i].check_status()

#check that all sensors can read
for sensor in sensor_suite:
	if sensor[i].read() != float:
		print "Does not work"
	else:
		print "Does work"
