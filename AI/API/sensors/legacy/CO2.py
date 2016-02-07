#/usr/bin/env python

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
