# To calibrate low, mid range of pH ( 2 point calibration) 
import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interfac
#e number			C     a    l    ,    h    i    g    h   1    0     .   0     0 
bus.write_i2c_block_data(0x65,0x43,[0x61,0x6C,0x2C,0x68,0x69,0x67,0x68,0x31,0x30,0x2E,0x30,0x30]) #Cal,high,10.00

time.sleep(1.3)

results=bus.read_i2c_block_data(0x65,0x52) #get calibration info

print results #print data

#time.sleep(5)
#
#bus.write_i2c_block_data(0x65,0x43,[0x61,0x6C,0x2C,0x3F])#Cal,? (Query the calibration)
#
#time.sleep(5.4)
#
#results=bus.read_i2c_block_data(0x65,0x52)
#
#time.sleep(3)
#
#print results
