# This script will enable the EC parameter, disable the dissolved solids, salinity and specific gravity parameters  
import smbus #import smbus library
import time
bus=smbus.SMBus(1) #assign an object to the SMBus class and mention the interface number
time.sleep(5)
bus.write_i2c_block_data(0x64,0x4F, [0x2C, 0x45, 0x43, 0x2C, 0x31]) # O,EC,1
time.sleep(5)
results=bus.read_i2c_block_data(0x64,0x52) #read cal info
time.sleep(5)
print results #print data
bus.write_i2c_block_data(0x64,0x4F, [0x2C, 0x54, 0x44, 0x53, 0x2C, 0x30]) # O, TDS, 0
time.sleep(5)
results=bus.read_i2c_block_data(0x64,0x52) #read cal info
time.sleep(5)
print results #print data
bus.write_i2c_block_data(0x64,0x4F, [0x2C, 0x53, 0x2C, 0x30]) # O, S, 0
time.sleep(5)
results=bus.read_i2c_block_data(0x64,0x52) #read cal info
time.sleep(5)
print results #print data
bus.write_i2c_block_data(0x64,0x4F, [0x2C, 0x53, 0x47, 0x2C, 0x30]) # O, SG, 0
time.sleep(5)
results=bus.read_i2c_block_data(0x64,0x52) #read cal info
time.sleep(5)
print results #print data
#READ EC VALUES NOW
bus.write_i2c_block_data(0x64,0x4F, [0x2C, 0x3F]) # O, SG, 0
time.sleep(5)
results=bus.read_i2c_block_data(0x64,0x52) #read cal info
time.sleep(5)
print results #print data