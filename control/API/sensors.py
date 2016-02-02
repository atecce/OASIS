# need this to wait
import time

# need this for I2C's
import smbus

# need this for camera
import cv2

# need this for UART
import Adafruit_BBIO.UART as UART

import serial

import struct 

class sensor:

	def __init__(self, pin):

		# these are determined at construction
		pin  = pin

	# This method depends on quite a bit. Depending on the data communication
	# type and the sensor, it will use different libraries and return different 
	# values.
	def read(self): pass

class I2C_sensor(sensor): 

	# Each I2C device has an address, register, and interface number

	address          = int()
	register	 = int()
	interface_number = int()

	def __init__(self, address, register, interface_number):

		# set address and register
		self.address          = address
		self.register	      = register

		# create bus with interface number
		self.bus = smbus.SMBus(interface_number) 

	def read(self):

		time.sleep(3)
		self.bus.write_byte(self.address, self.register) #R

		time.sleep(3)
		results = self.bus.read_i2c_block_data(self.address, self.register) #read cal info

		time.sleep(3)
		for index, item in enumerate(results):

			if item == 0:
				
				   end_val = index
				   break

		results = results[1:end_val]

		results_string = ''.join(chr(i) for i in results)

		return results_string

class ADC_sensor(sensor):

	# Each ADC device has an address, register, and interface number

	address    	 = int()
	register	 = int()
	interface_number = int()

	def __init__(self, address, register, interface_number):

		# set address and registers
		self.address  = address
		self.register = register

		# bus 2 is I2C bus on pins P9.17, P9.18
		bus = smbus.SMBus(interface_number) 

	def read(self):

		# 0x80 for LL1 sensor connected to VIN1 channel of ADC with I2C Address 0x22
		# 0xA0 for LL2 sensor connected to VIN3 channel of ADC with I2C Address 0x22
		# 0xC0 for LL3 sensor connected to VIN5 channel of ADC with I2C Address 0x22
		# 0xE0 for LL4 sensor connected to VIN7 channel of ADC with I2C Address 0x22
		# 0xF0 for LL5 sensor connected to VIN8 channel of ADC with I2C Address 0x22
		# 0xD0 for LL6 sensor connected to VIN6 channel of ADC with I2C Address 0x22
		# 0x80 for MO1 sensor connected to VIN1 channel of ADC with I2C Address 0x21
		# 0xA0 for MO2 sensor connected to VIN3 channel of ADC with I2C Address 0x21
		# 0xC0 for MO3 sensor connected to VIN5 channel of ADC with I2C Address 0x21
		# 0xE0 for MO4 sensor connected to VIN7 channel of ADC with I2C Address 0x21
		# 0xB0 for O2 OX1 sensor connected to VIN4 channel of ADC with I2C Address 0x22
		# 0xF0 for PAR1 sensor connected to VIN8 channel of ADC with I2C Address 0x21
		# 0xD0 for PAR2 sensor connected to VIN6 channel of ADC with I2C Address 0x21
		results = bus.read_i2c_block_data(address, register) 

		# LL sensors

		print "ADC Results from LL:", results

		sensordata = []

		for i in range(len(results)):

			if i % 2 == 0:

				a = bin(results[i])

				if(len(a)>5):

					a = a[len(a)-4:] # To get last 4 characters in the binary string

				b = bin(results[i+1])[2:]

				if(len(b)<8):

					for j in range(len(b), 8): b='0'+b

				c = a + b

				sensordata.append(int(c,2))

		print "\r\nLength of SensorData:", len(sensordata)
		print "SensorData:" + str(sensordata)
		sensordata.sort()
		print "Sorted SensorData:" + str(sensordata)

		sensorVal = (sensordata[7] +  sensordata[8])/(2.0)
		print "Chosen Sensor ADC Value:"+ str(sensorVal)
		analogVal = (sensorVal/4095.0)*3.3
		print "Chosen Sensor Analog Value in V:"+str(analogVal)

		actualAnalogVal = (3.3 - analogVal)/(2) + 1

		RES=2400
		supply_voltage=5
		I=(supply_voltage-actualAnalogVal)/RES

		resistance=actualAnalogVal/I;
		#resistance=1500-resistance;
		print "resistance is "
		print resistance

		# MO sensors

		print "ADC Results from MO sensor:", results
		print results
		sensordata = []
		for i in range(len(results)):
			#print "i value:"
			#print i
			if i%2 == 0:
				#print "inside if condition:"
				a = bin(results[i])
				if(len(a)>5):
					a = a[len(a)-4:] # To get last 4 characters in the binary string
				#print a

				b = bin(results[i+1])[2:]
				#print b

				len(b)

				if(len(b)<8):
					for j in range(len(b), 8):
						b='0'+b;

				c = a + b

				#print int(c,2)
				sensordata.append(int(c,2))

		print "\r\nLength of SensorData:"
		print len(sensordata)
		print "SensorData:"+str(sensordata)
		sensordata.sort()
		print "Sorted SensorData:"+str(sensordata)

		sensorVal = (sensordata[7] +  sensordata[8])/(2.0)
		print "Chosen Sensor ADC Value:"+ str(sensorVal)
		analogVal = (sensorVal/4095.0)*3.3
		print "Chosen Sensor Analog Value in V:"+str(analogVal)

		VWC=0 #VWC(Volumetric Water Content) = 0
		if (analogVal>=0 and analogVal<1.1):
			VWC=10*analogVal-1
		if (analogVal>=1.1 and analogVal<1.3):
			VWC=25*analogVal-17.5
		if (analogVal>=1.3 and analogVal<=1.82):
			VWC=48.08*analogVal-47.5

		# O2 sensor

		print "\r\nADC Results from O2 OX1 sensor:", results

		sensordata = []
		for i in range(len(results)):
			#print "i value:"
			#print i
			if i%2 == 0:
				#print "inside if condition:"
				a = bin(results[i])
				if(len(a)>5):
					a = a[len(a)-4:] # To get last 4 characters in the binary string
				#print a

				b = bin(results[i+1])[2:]
				#print b

				len(b)

				if(len(b)<8):
					for j in range(len(b), 8):
						b='0'+b;

				c = a + b

				#print int(c,2)
				sensordata.append(int(c,2))

		print "\r\nLength of SensorData:"
		print len(sensordata)
		print "SensorData:"+str(sensordata)
		sensordata.sort()
		print "Sorted SensorData:"+str(sensordata)

		sensorVal = (sensordata[7] +  sensordata[8])/(2.0)
		print "Chosen Sensor ADC Value:"+ str(sensorVal)
		analogVal = (sensorVal/4095.0)*3.3
		print "Chosen Sensor Analog Value in V:"+str(analogVal)

		gainVal = 40*5.86

		analogValmV = (analogVal/gainVal)*1000
		print "Chosen Sensor Analog Value in mV:"+str(analogValmV)

		slope = (9.0-0.0)/(20.0-0.0) # considering slope of linear line in the graph related to low range of sensor operation

		# PAR sensors

		print "ADC Results from PAR sensor:"
		print results
		sensordata = []
		for i in range(len(results)):
			#print "i value:"
			#print i
			if i%2 == 0:
				#print "inside if condition:"
				a = bin(results[i])
				if(len(a)>5):
					a = a[len(a)-4:] # To get last 4 characters in the binary string
				#print a

				b = bin(results[i+1])[2:]
				#print b

				len(b)

				if(len(b)<8):
					for j in range(len(b), 8):
						b='0'+b;

				c = a + b

				#print int(c,2)
				sensordata.append(int(c,2))

		print "\r\nLength of SensorData:"
		print len(sensordata)
		print "SensorData:"+str(sensordata)
		sensordata.sort()
		print "Sorted SensorData:"+str(sensordata)

		sensorVal = (sensordata[7] +  sensordata[8])/(2.0)
		print "Chosen Sensor ADC Value:"+ str(sensorVal)
		analogVal = (sensorVal/4095.0)*3.3
		print "Chosen Sensor Analog Value in V:"+str(analogVal)

		parValue = analogVal*1000*0.5

		print "PAR Value is "+str(parValue)+"micro-mol m^-2 s^-1"

class UART_sensor(sensor):

	def __init__(self, UART_number):

		UART.setup("UART" + str(UART_number))

		# CO2
		data = [0xfe, 0x44, 0x00, 0x08, 0x02, 0x9f, 0x25]
		d=struct.pack("7B", *data)
		ser = serial.Serial(port = "/dev/ttyO5", baudrate = 9600)
		#serial.begin(9600);
		#ser.close()
		#ser.open()
		time.sleep(1)
		while(ser.inWaiting() == 0):

			ser.write(d)
			time.sleep(1)

		A = ser.read(ser.inWaiting())
		percent = (ord(A[3])*256 + ord(A[4]))/10000.0
		print(str(percent) + "%")

		# flow meters

		# need to setup UART1 at boot, does not set up immediately
		# UART1 corresponds to ttyO1 in adafruit libraries
		# to manually enable use:
		# echo BB-UART1 > /sys/devices/bone_capemgr.*/slots 
		# ls /dev/tty*   in terminal 

		#while True:
		# baudrate corresponds to flow meter circuit baud rate 
		ser = serial.Serial(port = "/dev/ttyO1", baudrate = 38400)
		ser.open()
		boolean_is_open = ser.isOpen()
		print "Serial open?", boolean_is_open
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
		print "Flow rate [total vol] [LPM] [LPH]:", single_flow_reading
		ser.close()
		boolean_is_close = ser.isOpen()
		print "Serial open?", boolean_is_close

		# need to setup UART1 at boot, does not set up immediately
		# UART1 corresponds to ttyO1 in adafruit libraries
		# to manually enable use:
		# echo BB-UART1 > /sys/devices/bone_capemgr.*/slots 
		# ls /dev/tty*   in terminal 

		#while True:
		# baudrate corresponds to flow meter circuit baud rate 
		ser = serial.Serial(port = "/dev/ttyO4", baudrate = 38400)
		ser.open()
		boolean_is_open = ser.isOpen()
		print "Serial open?", boolean_is_open
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
		print "Flow Meter 2 Values:"
		print "Model Num is ", model_num
		print "Flow rate [total vol] [LPM] [LPH]:", single_flow_reading
		ser.close()
		boolean_is_close = ser.isOpen()
		print "Serial open?", boolean_is_close

class one_wire_sensor(sensor):

	def __init__(self, ID):

	# temperatures
	# (Note all the pins P8.3, P8.4, P8.5, P8.6 are shorted for intefacing all temp sensors on one-wire protocol)

	# Reading data from Temp 1 device with device ID:28-00000673a8a7 connected to P8.3 
	w1="/sys/bus/w1/devices/28-00000673a8a7/w1_slave" 

	# Reading data from Temp 2 device with device ID:28-0000065f27cc connected to P8.4 
	w1="/sys/bus/w1/devices/28-0000065f27cc/w1_slave" 

	# Reading data from Temp 3 device with device ID:28-0000065eb57a connected to P8.5 
	w1="/sys/bus/w1/devices/28-0000065eb57a/w1_slave" 

	# Reading data from Temp 4 device with device ID:28-000006747f7f connected to P8.6
	w1="/sys/bus/w1/devices/28-000006747f7f/w1_slave" 

	raw = open(w1, "r").read()
	print "Temperature is "+str(float(raw.split("t=")[-1])/1000)+" degrees"

class USB_sensor(sensor): 

	def __init__(self):

		camera = cv2.VideoCapture(0)

	def read(self):

		ret, frame = camera.read()
		cv2.imwrite("image1.jpeg", frame)
		camera.release()
		cv2.destroyAllWindows()

# liquid tanks and plumbing
S101 =      I2C_sensor(0x66, 0x52, 2)		# EC1
S102 =      I2C_sensor(0x65, 0x52, 2)		# pH1
S103 = one_wire_sensor("28-00000673a8a7")	# temp1
S104 =      I2C_sensor(0x61, 0x52, 2)		# DO
S105 =      ADC_sensor(0x22, 0x80, 2)	        # LL1
S106 =      ADC_sensor(0x22, 0xA0, 2)	        # LL2
S107 =      ADC_sensor(0x22, 0xC0, 2)	        # LL3
S108 =      ADC_sensor(0x22, 0xE0, 2)	        # LL4
S109 =      ADC_sensor(0x22, 0xF0, 2)	        # LL5
S110 =     UART_sensor(1)			# flow_met1
S111 =     UART_sensor(4)			# flow_met2
S112 = 	    ADC_sensor(0x22, 0xD0, 2)		# LL6

# growth medium
S201 = one_wire_sensor("28-0000065f27cc")	# temp2
S202 = one_wire_sensor("28-0000065eb57a")	# temp3
S203 = one_wire_sensor("28-000006747f7f")	# temp4
#S204 = one_wire_sensor()	# temp5
S205 = I2C_sensor(0x64, 0x52, 2)	# EC2
S206 = I2C_sensor(0x63, 0x52, 2)	# pH2
S208 = ADC_sensor(0x21, 0x80, 2)	# MO1
S209 = ADC_sensor(0x21, 0xA0, 2)	# MO2
S210 = ADC_sensor(0x21, 0xC0, 2)	# MO3
S211 = ADC_sensor(0x21, 0xE0, 2)	# MO4

# internal atmosphere
#S301 = one_wire_sensor()	# RHTemp1
#S302 = one_wire_sensor("P8_9")	# RHTemp2
#S303 = I2C_sensor()	# TP1
S304 = ADC_sensor(0x22, 0xB0, 2)	# O2
S305 = UART_sensor(5)	# C02
S306 = ADC_sensor(0x21, 0xF0, 2)	# PAR1
S307 = USB_sensor()		# camera

# external environment
#S401 = one_wire_sensor("P8_10")	# RHTemp3
#S402 = I2C_sensor()		# TP2
S403 = ADC_sensor(0x21, 0xD0, 2)	# PAR2

sensor_suite = (S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, 
		S201, S202, S203,       S205, S206,       S208, S209, S210, S211,
		                  S304, S305, S306, S307,
		            S403)

for sensor in sensor_suite: sensor.read()
