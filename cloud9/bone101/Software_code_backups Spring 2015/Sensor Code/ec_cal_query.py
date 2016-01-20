# This script queries
import smbus #import smbus library
import time
bus=smbus.SMBus(1) #assign an object to the SMBus class and mention the interface number
bus.write_i2c_block_data(0x64,0x43,[0x61,0x6c,0x2c,0x3f]) # Cal, ?
results=bus.read_i2c_block_data(0x64,0x52) #get calibration info
print results #print data