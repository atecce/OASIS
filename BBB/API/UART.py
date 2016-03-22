# need this to wait
import time

# need this for UART
import Adafruit_BBIO.UART as UART

# need this to read serial buffer
import serial

# what is this?
import struct 

class UART_sensor:

	def __init__(self, UART_number):

		# initiate sensor with a UART value
		UART.setup("UART" + str(UART_number))

		# UART number corresponds to terminal number (convenient)
		self.tty = UART_number

class carbon_dioxide(UART_sensor):

	# ATLAS CO2 sensors have a baudrate of 9600
	baudrate = 9600

	def read(self):

		# what determines this list of hexadecimel numbers?
		data = [0xfe, 0x44, 0x00, 0x08, 0x02, 0x9f, 0x25]

		# what does struct do? why 7B? what's the asterisk do?
		d = struct.pack("7B", *data)

		# initalize serial port
		ser = serial.Serial(port = "/dev/ttyO" + str(self.tty), baudrate = self.baudrate)

		# wait
		time.sleep(1)

		# open the serial port
		ser.open()

		# while serial buffer is empty
		while(ser.inWaiting() == 0):

			# write data
			ser.write(d)

			# wait
			time.sleep(1)

		# read in remaining characters in buffer
		A = ser.read(ser.inWaiting())

		# third bit times 2^8 (a byte) + fourth bit divided by 10^4
		percent = (ord(A[3])*256 + ord(A[4]))/10000.0

		# close serial port
		ser.close()

		# return percentage
		return percent

class flow_meter(UART_sensor):

	# ATLAS flow meters have a baudrate of 38400
	baudrate = 38400

	def read(self):

		# need to setup UART1 at boot, does not set up immediately
		# UART1 corresponds to ttyO1 in adafruit libraries
		# to manually enable use:
		# echo BB-UART1 > /sys/devices/bone_capemgr.*/slots 
		# ls /dev/tty*   in terminal 

		# need to setup UART1 at boot, does not set up immediately
		# UART1 corresponds to ttyO1 in adafruit libraries
		# to manually enable use:
		# echo BB-UART1 > /sys/devices/bone_capemgr.*/slots 
		# ls /dev/tty*   in terminal 

		# baudrate corresponds to flow meter circuit baud rate 
		ser = serial.Serial(port = "/dev/ttyO" + str(self.tty), baudrate = self.baudrate)

		# open serial port
		ser.open()

		# turn on LEDs. Green = power, red = instruction received/data transmit, 
		# amber = one rotation of meter blades
		ser.write("L1\r")

		# wait
		time.sleep(1)

		# write model number TurboFlow 226000
		ser.write("T1\r")

		# wait
		time.sleep(1)

		# return num of chars in receive buffer
		num = ser.inWaiting()

		# read Turboflow
		model_num = ser.read(num)

		# wait
		time.sleep(1)

		# what are we writing?
		ser.write("R\r")

		# wait
		time.sleep(1)

		# return num of chars in receive buffer
		num = ser.inWaiting()

		# returns entire serial buffer?
		single_flow_reading = ser.read(num)
		
		# is this just a diagnostic thing?
		# print "Model Num is ", model_num

		# close serial port
		ser.close()

		# flow rate [total vol] [LPM] [LPH]
		return single_flow_reading

class moisture(UART_sensor): pass
class photosynthetically_active_radiation(UART_sensor): pass
class relative_humidity_and_temperature(UART_sensor): pass
