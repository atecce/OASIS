import urllib2,urllib

fo = open("test.txt", "wb");
fo.write("MO1 Successful!!!");
print "Hello Welcome to Python Testing.. !!!"

import Adafruit_BBIO.UART as UART
# need to setup UART1 at boot, does not set up immediately
# UART1 corresponds to ttyO1 in adafruit libraries
# to manually enable use:
# echo BB-UART1 > /sys/devices/bone_capemgr.*/slots 
# ls /dev/tty*   in terminal 

UART.setup("UART4")
import time
import serial  #use pyserial to communicate

# baudrate corresponds to flow meter circuit baud rate 
ser = serial.Serial(port = "/dev/ttyO4", baudrate=38400)
ser.open()
boolean_is_open = ser.isOpen()
print "Serial open?" , boolean_is_open
# turn on LEDs. Green = power, red = instruction received/data transmit, 
# amber = one rotation of meter blades
ser.write("L1\r")
time.sleep(.4)
# write model number TurboFlow 226000
ser.write("T1\r")
time.sleep(0.4)
# return num of chars in receive buffer
num = ser.inWaiting()
# read Turboflow
model_num = ser.read(num)
time.sleep(0.4)
ser.write("R\r")
time.sleep(2)
# return num of chars in receive buffer
num = ser.inWaiting()
single_flow_reading = ser.read(num)
# print values 
print "Model Num is ", model_num
print "Flow rate [total vol] [LPM] [LPH]:" , single_flow_reading
ser.close()
boolean_is_close = ser.isOpen()
print "Serial open?" , boolean_is_close

dataValue = "Flow rate [total vol] [LPM] [LPH]:" + single_flow_reading

mydata=[('sensor','ltp_fm2'),('value',dataValue)]    #The first is the var name the second is the value
mydata=urllib.urlencode(mydata)
path="http://192.168.7.2:8080/MarsOASIS/pages/py/saveSensorData.php"    #the url you want to POST to
req=urllib2.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
proxy_support = urllib2.ProxyHandler({})
opener = urllib2.build_opener(proxy_support)
page=opener.open(req).read()
print page