# need this to wait
import time

# need this for I2C's
import smbus

# need this for camera
import cv2

# need this for UART
import Adafruit_BBIO.UART as UART

# need this for temperature
import Adafruit_DHT

# need this to read serial buffer
import serial

# what is this?
import struct 

# need to import everything to declare these

S105 = liquid_level(0x22, 0x80, 2)	        # LL1
S106 = liquid_level(0x22, 0xA0, 2)	        # LL2
S107 = liquid_level(0x22, 0xC0, 2)	        # LL3
S108 = liquid_level(0x22, 0xE0, 2)	        # LL4
S109 = liquid_level(0x22, 0xF0, 2)	        # LL5
S112 = liquid_level(0x22, 0xD0, 2)		# LL6

# is CO2 broken?
S110 = UART_sensor(1)				# flow_met1
S111 = UART_sensor(4)				# flow_met2
#S305 = UART_sensor(5)				# C02

# why no temperature 5?
S103 = temperature("28-00000673a8a7")		# temp1
S201 = temperature("28-0000065f27cc")		# temp2
S202 = temperature("28-0000065eb57a")		# temp3
S203 = temperature("28-000006747f7f")		# temp4
#S204 = one_wire_sensor()			# temp5

S104 = I2C_sensor(0x61, 0x52, 2)		# DO
S102 = I2C_sensor(0x65, 0x52, 2)		# pH1
S206 = I2C_sensor(0x63, 0x52, 2)		# pH2
S101 = I2C_sensor(0x66, 0x52, 2)		# EC1
S205 = I2C_sensor(0x64, 0x52, 2)		# EC2
#S303 = I2C_sensor()				# TP1
#S402 = I2C_sensor()				# TP2

S208 = MO_sensor(0x21, 0x80, 2)			# MO1
S209 = MO_sensor(0x21, 0xA0, 2)			# MO2
S210 = MO_sensor(0x21, 0xC0, 2)			# MO3
S211 = MO_sensor(0x21, 0xE0, 2)			# MO4

# internal atmosphere
S301 = RH_and_temp('P8_8')			# RHTemp1
S302 = RH_and_temp('P8_9')			# RHTemp2
#S401 = one_wire_sensor("P8_10")		# RHTemp3
S304 = ADC_sensor(0x22, 0xB0, 2)		# O2
S306 = ADC_sensor(0x21, 0xF0, 2)		# PAR1
#S403 = ADC_sensor(0x21, 0xD0, 2)		# PAR2
S307 = USB_sensor()				# camera
