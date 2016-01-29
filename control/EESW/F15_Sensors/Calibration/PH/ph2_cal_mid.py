# To calibrate low, mid range of pH ( 2 point calibration) 
import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interfac
#e number
bus.write_i2c_block_data(0x63,0x43,[0x61,0x6C,0x2C,0x6D,0x69,0x64,0x2C,0x37,0x2E,0x30,0x30]) #Cal,mid,7.00
time.sleep(5)
results=bus.read_i2c_block_data(0x63,0x52) #get calibration info
print results #print data
time.sleep(5)
bus.write_i2c_block_data(0x63,0x43,[0x61,0x6C,0x2C,0x3F])#Cal,? (Query the calibration)
time.sleep(5.4)
results=bus.read_i2c_block_data(0x63,0x52)
time.sleep(3)
print results
