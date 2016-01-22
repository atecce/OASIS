import time

w1="/sys/bus/w1/devices/28-0000065eb57a/w1_slave" #Reading data from Temp 3 device with device ID:28-0000065eb57a connected to P8.5 (Note all the pins P8.3, P8.4, P8.5, P8.6 are shorted for intefacing all temp sensors on one-wire protocol)

raw = open(w1, "r").read()
print "Temperature is "+str(float(raw.split("t=")[-1])/1000)+" degrees"


#uncomment the below code for continuous reading of values
"""
while True:
    raw = open(w1, "r").read()
    print "Temperature is "+str(float(raw.split("t=")[-1])/1000)+" degrees"
    time.sleep(1)"""