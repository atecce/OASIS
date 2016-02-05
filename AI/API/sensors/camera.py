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

class USB_sensor: 

	# may not need a constructor here
	def __init__(self): pass

	def read(self):

		# set camera?
		self.camera = cv2.VideoCapture(0)

		# ret and frame? what does read return?
		ret, frame = self.camera.read()

		# write to a file, why do we need frame?
		cv2.imwrite("image1.jpeg", frame)

		# release the camera
		self.camera.release()

		# close cv2?
		cv2.destroyAllWindows()
