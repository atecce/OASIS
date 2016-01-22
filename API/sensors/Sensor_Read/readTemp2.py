import time

w1="/sys/bus/w1/devices/28-0000065f27cc/w1_slave" #Reading data from Temp 2 device with device ID:28-0000065f27cc connected to P8.4 (Note all the pins P8.3, P8.4, P8.5, P8.6 are shorted for intefacing all temp sensors on one-wire protocol)

raw = open(w1, "r").read()
print "Temperature is "+str(float(raw.split("t=")[-1])/1000)+" degrees"


#uncomment the below code for continuous reading of values
"""
while True:
    raw = open(w1, "r").read()
    print "Temperature is "+str(float(raw.split("t=")[-1])/1000)+" degrees"
    time.sleep(1)"""
