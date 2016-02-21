#This script clear calibration and then calibrates dry
import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
bus.write_i2c_block_data(0x64,0x43,[0x61,0x6C,0x2C,0x63,0x6C,0x65, 0X61, 0x72 ]) #Cal, clear
time.sleep(5.4)
results=bus.read_i2c_block_data(0x64,0x52)
time.sleep(3)
bus.write_i2c_block_data(0x64,0x43,[0x61,0x6C,0x2C,0x64,0x72,0x79 ]) #Cal, dry
time.sleep(5)
results=bus.read_i2c_block_data(0x64,0x52) #get calibration info
print results #print data
for index, item in enumerate(results):
        if item == 0:
                end_val = index
                break
results = results[1:end_val]
results_string = ''.join(chr(i) for i in results)
print results_string #print data
