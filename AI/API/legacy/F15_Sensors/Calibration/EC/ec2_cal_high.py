# This script will execute high point calibration
import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
time.sleep(5)
bus.write_i2c_block_data(0x64,0x43,[0x61,0x6C,0x2C,0x68, 0x69, 0x67, 0x68, 0x2C, 0x38, 0x30, 0x30, 0x30, 0x30]) #Cal, high, n (80000)
time.sleep(5)
results=bus.read_i2c_block_data(0x64,0x52) #read cal info
time.sleep(5)
print results #print data