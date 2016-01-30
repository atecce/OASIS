class sensor:

	def __init__(self, name, pin):

		# these are determined at construction
		name = name
		pin  = pin

	# This method depends on quite a bit. Depending on the data communication
	# type and the sensor, it will use different libraries and return different 
	# values.
	def read(self): pass

class I2C_sensor(sensor): pass

class ADC_sensor(sensor): pass

class UART_sensor(sensor): pass

class one_wire_sensor(sensor): pass

class USB_sensor(sensor): pass

# liquid tanks and plumbing
S101 = I2C_sensor("S101", "0x66")	# EC1
S102 = I2C_sensor("S102", "0x65")	# pH1
S103 = one_wire_sensor("S103", NULL)	# temp1
S104 = I2C_sensor("S104", "0x61")	# DO
S105 = ADC_sensor("S105", NULL)		# LL1
S106 = ADC_sensor("S106", NULL)		# LL2
S107 = ADC_sensor("S107", NULL)		# LL3
S108 = ADC_sensor("S108", NULL)		# LL4
S109 = ADC_sensor("S109", NULL)		# LL5
S110 = UART_sensor("S110", NULL)	# flow_met1
S111 = UART_sensor("S111", NULL)	# flow_met2
S112 = ADC_sensor("S112", NULL)		# LL6

# growth medium
S201 = one_wire_sensor("S201", NULL)	# temp2
S202 = one_wire_sensor("S202", NULL)	# temp3
S203 = one_wire_sensor("S203", NULL)	# temp4
S204 = one_wire_sensor("S204", NULL)	# temp5
S205 = I2C_sensor("S205", NULL)		# EC2
S206 = I2C_sensor("S206", NULL)		# pH2
S208 = ADC_sensor("S208", NULL)		# MO1
S209 = ADC_sensor("S209", NULL)		# MO2
S210 = ADC_sensor("S210", NULL)		# MO3
S211 = ADC_sensor("S211", NULL)		# MO4

# internal atmosphere
S301 = one_wire_sensor("S301", NULL)	# RHTemp1
S302 = one_wire_sensor("S302", "P8_9")	# RHTemp2
S303 = I2C_sensor("S303", "0x77")	# TP1
S304 = ADC_sensor("S304", NULL)		# O2
S305 = UART_sensor("S305", NULL)	# C02
S306 = ADC_sensor("S306", NULL)		# PAR1
S307 = USB_sensor("S307", NULL)		# camera

# external environment
S401 = one_wire_sensor("S401", "P8_10")	# RHTemp3
S402 = I2C_sensor("S402", NULL)		# TP2
S403 = ADC_sensor("S403", NULL)		# PAR2

sensor_suite = (S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, 
		S201, S202, S203, S204, S205, S206,       S208, S209, S210, S211,
		S301, S302, S303, S304, S305, S306, S307,
		S401, S402, S403)
