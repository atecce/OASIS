import time
import smbus

class sensor:

	def __init__(self, name, pin):

		# these are determined at construction
		name = name
		pin  = pin

	# This method depends on quite a bit. Depending on the data communication
	# type and the sensor, it will use different libraries and return different 
	# values.
	def read(self): pass

class I2C_sensor(sensor): 

	slave_address    = int()
	interface_number = int()

	def __init__(self, slave_address, interface_number):

		self.slave_address    = slave_address
		self.interface_number = interface_number

		# create bus with interface number
		self.bus = smbus.SMBus(interface_number) 

	def read(self):

		time.sleep(3)
		self.bus.write_byte(self.slave_address, 0x52) #R

		time.sleep(3)
		results = self.bus.read_i2c_block_data(self.slave_address, 0x52) #read cal info

		time.sleep(3)
		for index, item in enumerate(results):

			if item == 0:
				
				   end_val = index
				   break

		results = results[1:end_val]

		results_string = ''.join(chr(i) for i in results)

		return results_string

class ADC_sensor(sensor): pass

class UART_sensor(sensor): pass

class one_wire_sensor(sensor): pass

class USB_sensor(sensor): pass

# liquid tanks and plumbing
S101 = I2C_sensor(0x66, 2)	# EC1
S102 = I2C_sensor(0x65, 2)	# pH1
#S103 = one_wire_sensor()	# temp1
S104 = I2C_sensor(0x61, 2)	# DO

#S105 = ADC_sensor()		# LL1
#S106 = ADC_sensor()		# LL2
#S107 = ADC_sensor()		# LL3
#S108 = ADC_sensor()		# LL4
#S109 = ADC_sensor()		# LL5
#S110 = UART_sensor()	# flow_met1
#S111 = UART_sensor()	# flow_met2
#S112 = ADC_sensor()		# LL6

# growth medium
#S201 = one_wire_sensor()	# temp2
#S202 = one_wire_sensor()	# temp3
#S203 = one_wire_sensor()	# temp4
#S204 = one_wire_sensor()	# temp5
S205 = I2C_sensor(0x64, 2)		# EC2
S206 = I2C_sensor(0x63, 2)		# pH2
#S208 = ADC_sensor()		# MO1
#S209 = ADC_sensor()		# MO2
#S210 = ADC_sensor()		# MO3
#S211 = ADC_sensor()		# MO4

# internal atmosphere
#S301 = one_wire_sensor()	# RHTemp1
#S302 = one_wire_sensor("P8_9")	# RHTemp2
#S303 = I2C_sensor()	# TP1
#S304 = ADC_sensor()		# O2
#S305 = UART_sensor()	# C02
#S306 = ADC_sensor()		# PAR1
#S307 = USB_sensor()		# camera

# external environment
#S401 = one_wire_sensor("P8_10")	# RHTemp3
#S402 = I2C_sensor()		# TP2
#S403 = ADC_sensor()		# PAR2

print S101.read(), S102.read(), S104.read(), S205.read(), S206.read()

#sensor_suite = (S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, 
#		S201, S202, S203, S204, S205, S206,       S208, S209, S210, S211,
#		S301, S302, S303, S304, S305, S306, S307,
#		S401, S402, S403)
