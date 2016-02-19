import urllib2,urllib

fo = open("test.txt", "wb");
fo.write("MO1 Successful!!!");
print "Hello Welcome to Python Testing.. !!!"

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
print results_string

dataValue = results_string

mydata=[('sensor','gm_pH'),('value',dataValue)]    #The first is the var name the second is the value
mydata=urllib.urlencode(mydata)
path="http://192.168.7.2:8080/MarsOASIS/pages/py/saveSensorData.php"    #the url you want to POST to
req=urllib2.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
proxy_support = urllib2.ProxyHandler({})
opener = urllib2.build_opener(proxy_support)
page=opener.open(req).read()
print page