# This script will send the circuit the temp of the liquid for more accurate EC readings
import smbus #import smbus library
import time
bus=smbus.SMBus(1) #assign an object to the SMBus class and mention the interface number
time.sleep(5)
bus.write_i2c_block_data(0x64,0x54,[0x2C, 0x31, 0x39, 0x2E,0x35]) #T, n (19.5) <- change this
time.sleep(5)
results=bus.read_i2c_block_data(0x64,0x52) #read cal info
time.sleep(5)
print results #print data