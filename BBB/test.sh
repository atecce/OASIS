#!/bin/bash
# 
# this runs the sensedaemons and detaches from any specific terminal
#
# make sure to while you have sudo privileges (a hacky way is just to type "sudo ls" before running this) 
# otherwise, you will be prompted for a password, and it will just write that prompt to the sensor data over and over again

# set current path to working directory
PWD=`pwd`

# for each data communication type
for data_comm in $PWD/sensedaemons/*; do

	# for each sensor
	for sensor in $data_comm/*; do

		# run daemon
		echo "nohup $sensor > /dev/null 2>$data_comm/errorlog.txt &"

	done
done
