# To calibrate low, mid range of pH ( 2 point calibration) 
import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interfac
#e number			C     a    l    ,    c    l    e    a   r    
#bus.write_i2c_block_data(0x65,0x43,[0x61,0x6C,0x2C,0x63,0x6C,0x65,0x61,0x72]) #Cal,clear

#e number			C     a    l    ,    ?    
bus.write_i2c_block_data(0x65,0x43,[0x61,0x6C,0x2C,0x3F]) #Cal,?

time.sleep(5)
results=bus.read_i2c_block_data(0x65,0x52) #get calibration info
print str(results) #print data

