import urllib2,urllib


import Adafruit_BBIO.UART as UART
import serial
import time
import struct 
UART.setup("UART5")
data=[0xfe,0x44,0x00,0x08,0x02,0x9f,0x25]
d=struct.pack("7B",*data)
ser = serial.Serial(port = "/dev/ttyO5", baudrate=9600)
#serial.begin(9600);
#ser.close()
#ser.open()
time.sleep(1)
while(ser.inWaiting()==0):
	ser.write(d)
	time.sleep(1)
A=ser.read(ser.inWaiting())
percent=(ord(A[3])*256+ord(A[4]))/10000.0
print(str(percent)+ "%")

dataValue = str(round(percent,3))+ "%"

mydata=[('sensor','ie_co'),('value',dataValue)]    #The first is the var name the second is the value
mydata=urllib.urlencode(mydata)
path="http://192.168.7.2:8080/MarsOASIS/pages/py/saveSensorData.php"    #the url you want to POST to
req=urllib2.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
proxy_support = urllib2.ProxyHandler({})
opener = urllib2.build_opener(proxy_support)
page=opener.open(req).read()
print page

fo = open("test.txt", "wb");
fo.write("CO2@@@ Successful!!!");
print "Hello Welcome to Python Testing.. !!!"