# script to calibrate DO
import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interfac
#e number
bus.write_i2c_block_data(0x61,0x43,[0x61,0x6C,0x2C,0x63,0x6C,0x65, 0X61, 0x72 ])#Cal, clear
time.sleep(5.4)
results=bus.read_i2c_block_data(0x61,0x52)
time.sleep(3)
print results
time.sleep(3)
bus.write_i2c_block_data(0x61,0x43,[0x61,0x6C]) #Cal (Calibrates the device to atmospheric oxygen levels)
time.sleep(5)
results=bus.read_i2c_block_data(0x61,0x52) #get calibration info
print results #print data
time.sleep(3)
bus.write_i2c_block_data(0x61,0x43,[0x61,0x6C,0x2C,0x3F]) #Cal,? (Query the calibration)
time.sleep(5)
results=bus.read_i2c_block_data(0x61,0x52) #get calibration info
print results #print data