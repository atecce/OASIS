import Adafruit_BBIO.UART as UART
import serial
import time
import struct 
UART.setup("UART1")

data=[0xfe,0x44,0x00,0x08,0x02,0x9f,0x25]
d=struct.pack("7B",*data) 
ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
#serial.begin(9600);
#ser.close()
#ser.open()
time.sleep(1)
while(ser.inWaiting()==0):
	"""ser.write("0xfe")
	ser.write("0x44")
	ser.write("0x00")
	ser.write("0x08")
	ser.write("0x32")
	ser.write("0x9f")
	ser.write("0x25")"""
	ser.write(d)
	time.sleep(1)
A=ser.read(ser.inWaiting())
for c in A:
	print ord(c)


