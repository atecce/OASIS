import Adafruit_BBIO.UART as UART
# need to setup UART1 at boot, does not set up immediately
# UART1 corresponds to ttyO1 in adafruit libraries
# to manually enable use:
# echo BB-UART1 > /sys/devices/bone_capemgr.*/slots 
# ls /dev/tty*   in terminal 

UART.setup("UART1")
import time
import serial  #use pyserial to communicate

#while True:
# baudrate corresponds to flow meter circuit baud rate 
ser = serial.Serial(port = "/dev/ttyO1", baudrate=38400)
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
print "Flow Meter 1 Values:"
print "Model Num is ", model_num
print "Flow rate [total vol] [LPM] [LPH]:" , single_flow_reading
ser.close()
boolean_is_close = ser.isOpen()
print "Serial open?" , boolean_is_close
