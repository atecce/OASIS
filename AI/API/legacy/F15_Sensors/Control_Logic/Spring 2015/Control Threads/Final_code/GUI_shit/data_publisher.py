from urllib2 import Request, urlopen
import math
import time

names={"temp":22,"test_pressure":50,"test_ph":70,"test_ec":200, "test_temp":40, "test_ph2":30, "test_temp1":350, "test_temp2":90, "ph":6, "ec":7 }
#temp=temp, pressure=test_pressure, humidity= test_ph, co2= test_ec, o2= test_temp, n2=test_ph2, par=test_temp1 ,d_o=test_temp2, ph=ph, ec=ec

i=1

while(i):
    for key,val in names.iteritems():
        test_value=math.sin(i)+val
        json="{\"data_point\":{\"name\":\""+str(key)+"\", \"value\":"+str(test_value)+",\"timestamp\":"+str(int(time.time()))+"}}"
        headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Token token="91cde66f8744bddb93103e41e91e6016"'
        }
        request = Request('http://api.autoponics.com/data_points', data=json, headers=headers)
        response_body = urlopen(request).read()
        print response_body
    i+=0.05
    time.sleep(3)  


