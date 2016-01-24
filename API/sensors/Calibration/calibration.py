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


import smbus #import smbus library
import time

slave_add=0x61
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
time.sleep(3)
bus.write_byte(slave_add,0x52) #R
time.sleep(3)
results=bus.read_i2c_block_data(slave_add,0x52) #read cal info
time.sleep(3)
#print results
for index, item in enumerate(results):
	if item == 0:
		   end_val = index
		   break
results = results[1:end_val]
results_string = ''.join(chr(i) for i in results)
# #print" in main try"
print results_string


#This script clear calibration and then calibrates dry
import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
bus.write_i2c_block_data(0x66,0x43,[0x61,0x6C,0x2C,0x63,0x6C,0x65, 0X61, 0x72 ]) #Cal, clear
time.sleep(5.4)
results=bus.read_i2c_block_data(0x66,0x52)
time.sleep(3)
bus.write_i2c_block_data(0x66,0x43,[0x61,0x6C,0x2C,0x64,0x72,0x79 ]) #Cal, dry
time.sleep(5)
results=bus.read_i2c_block_data(0x66,0x52) #get calibration info
print results #print data
for index, item in enumerate(results):
        if item == 0:
                end_val = index
                break
results = results[1:end_val]
results_string = ''.join(chr(i) for i in results)
print results_string #print data


# This script will execute high point calibration
import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
time.sleep(5)
bus.write_i2c_block_data(0x66,0x43,[0x61,0x6C,0x2C,0x68, 0x69, 0x67, 0x68, 0x2C, 0x38, 0x30, 0x30, 0x30, 0x30]) #Cal, high, n (80000)
time.sleep(5)
results=bus.read_i2c_block_data(0x66,0x52) #read cal info
time.sleep(5)
print results #print data# This script calibrates low point (dual pt calibration)



import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
#bus.write_i2c_block_data(0x64,0x43,[0x61,0x6c,0x2c,0x3f]) # Cal, ?
#results=bus.read_i2c_block_data(0x64,0x52) #get calibration info
#print results #print data
# bus.write_i2c_block_data(0x64,0x43,[0x61,0x6C,0x2C,0x63,0x6C,0x65, 0X61, 0x72 ]) #Cal, clear
# time.sleep(5.4)
# results=bus.read_i2c_block_data(0x64,0x52)
#time.sleep(5)
bus.write_i2c_block_data(0x66,0x43,[0x61,0x6C,0x2C,0x6C, 0x6F, 0x77, 0x2C, 0x31, 0x32, 0x38, 0x38, 0x30]) #Cal, low, n
time.sleep(5)
results=bus.read_i2c_block_data(0x66,0x52) #read cal info
print results #print dataimport smbus #import smbus library



import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
#time.sleep(5)
bus.write_byte(0x66,0x52) #R
time.sleep(2)
results=bus.read_i2c_block_data(0x66,0x52) #read cal info
time.sleep(2)
print results #print data
for index, item in enumerate(results):
        if item == 0:
                end_val = index
                break
results = results[1:end_val]
results_string = ''.join(chr(i) for i in results)
print results_string #print data




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




# This script will execute high point calibration
import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
time.sleep(5)
bus.write_i2c_block_data(0x64,0x43,[0x61,0x6C,0x2C,0x68, 0x69, 0x67, 0x68, 0x2C, 0x38, 0x30, 0x30, 0x30, 0x30]) #Cal, high, n (80000)
time.sleep(5)
results=bus.read_i2c_block_data(0x64,0x52) #read cal info
time.sleep(5)
print results #print data# This script calibrates low point (dual pt calibration)




import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
#bus.write_i2c_block_data(0x64,0x43,[0x61,0x6c,0x2c,0x3f]) # Cal, ?
#results=bus.read_i2c_block_data(0x64,0x52) #get calibration info
#print results #print data
# bus.write_i2c_block_data(0x64,0x43,[0x61,0x6C,0x2C,0x63,0x6C,0x65, 0X61, 0x72 ]) #Cal, clear
# time.sleep(5.4)
# results=bus.read_i2c_block_data(0x64,0x52)
#time.sleep(5)
bus.write_i2c_block_data(0x64,0x43,[0x61,0x6C,0x2C,0x6C, 0x6F, 0x77, 0x2C, 0x31, 0x32, 0x38, 0x38, 0x30]) #Cal, low, n
time.sleep(5)
results=bus.read_i2c_block_data(0x64,0x52) #read cal info
print results #print dataimport smbus #import smbus library




import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
#time.sleep(5)
bus.write_byte(0x64,0x52) #R
time.sleep(2)
results=bus.read_i2c_block_data(0x64,0x52) #read cal info
time.sleep(2)
print results #print data
for index, item in enumerate(results):
        if item == 0:
                end_val = index
                break
results = results[1:end_val]
results_string = ''.join(chr(i) for i in results)
print results_string #print data




import smbus #import smbus library
import time

slave_add=0x65
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
time.sleep(3)
bus.write_byte(slave_add,0x52) #R
time.sleep(3)
results=bus.read_i2c_block_data(slave_add,0x52) #read cal info
time.sleep(3)
#print results
for index, item in enumerate(results):
	if item == 0:
		   end_val = index
		   break
results = results[1:end_val]
results_string = ''.join(chr(i) for i in results)
# #print" in main try"
print results_stringimport smbus #import smbus library




import time

slave_add=0x63
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
time.sleep(3)
bus.write_byte(slave_add,0x52) #R
time.sleep(3)
results=bus.read_i2c_block_data(slave_add,0x52) #read cal info
time.sleep(3)
#print results
for index, item in enumerate(results):
	if item == 0:
		   end_val = index
		   break
results = results[1:end_val]
results_string = ''.join(chr(i) for i in results)
# #print" in main try"
print results_string# To calibrate low, mid range of pH (2 point calibration) 



import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interfac
#e number
#bus.write_i2c_block_data(0x63,0x43,[0x61,0x6C,0x2C,0x6C,0x6F,0x77,0x2C,0x35,0x2E,0x30,0x30]) #Cal,low,5.00
bus.write_i2c_block_data(0x65,0x43,[0x61,0x6C,0x2C,0x6C,0x6F,0x77,0x2C,0x33,0x2E,0x30,0x30]) #Cal,low,3.00
time.sleep(5)
results=bus.read_i2c_block_data(0x65,0x52) #get calibration info
time.sleep(5)
print results #print data
bus.write_i2c_block_data(0x65,0x43,[0x61,0x6C,0x2C,0x3F])#Cal,? (Query the calibration)
time.sleep(5.4)
results=bus.read_i2c_block_data(0x65,0x52)
time.sleep(3)
print results



# To calibrate low, mid range of pH ( 2 point calibration) 
import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interfac
#e number
bus.write_i2c_block_data(0x65,0x43,[0x61,0x6C,0x2C,0x6D,0x69,0x64,0x2C,0x37,0x2E,0x30,0x30]) #Cal,mid,7.00
time.sleep(5)
results=bus.read_i2c_block_data(0x65,0x52) #get calibration info
print results #print data
time.sleep(5)
bus.write_i2c_block_data(0x65,0x43,[0x61,0x6C,0x2C,0x3F])#Cal,? (Query the calibration)
time.sleep(5.4)
results=bus.read_i2c_block_data(0x65,0x52)
time.sleep(3)
print results
# To calibrate low, mid range of pH (2 point calibration) 



import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interfac
#e number
#bus.write_i2c_block_data(0x63,0x43,[0x61,0x6C,0x2C,0x6C,0x6F,0x77,0x2C,0x35,0x2E,0x30,0x30]) #Cal,low,5.00
bus.write_i2c_block_data(0x63,0x43,[0x61,0x6C,0x2C,0x6C,0x6F,0x77,0x2C,0x33,0x2E,0x30,0x30]) #Cal,low,3.00
time.sleep(5)
results=bus.read_i2c_block_data(0x63,0x52) #get calibration info
time.sleep(5)
print results #print data
bus.write_i2c_block_data(0x63,0x43,[0x61,0x6C,0x2C,0x3F])#Cal,? (Query the calibration)
time.sleep(5.4)
results=bus.read_i2c_block_data(0x63,0x52)
time.sleep(3)
print results



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
