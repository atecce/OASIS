import urllib2,urllib

fo = open("test.txt", "wb");
fo.write("MO1 Successful!!!");
print "Hello Welcome to Python Testing.. !!!"

import time

w1="/sys/bus/w1/devices/28-0000065f27cc/w1_slave" #Reading data from Temp 2 device with device ID:28-0000065f27cc connected to P8.4 (Note all the pins P8.3, P8.4, P8.5, P8.6 are shorted for intefacing all temp sensors on one-wire protocol)

raw = open(w1, "r").read()
print "Temperature is "+str(float(raw.split("t=")[-1])/1000)+" degrees"

dataValue = str(float(raw.split("t=")[-1])/1000) + " *C"

mydata=[('sensor','gm_temp2'),('value',dataValue)]    #The first is the var name the second is the value
mydata=urllib.urlencode(mydata)
path="http://192.168.7.2:8080/MarsOASIS/pages/py/saveSensorData.php"    #the url you want to POST to
req=urllib2.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
proxy_support = urllib2.ProxyHandler({})
opener = urllib2.build_opener(proxy_support)
page=opener.open(req).read()
print page