from urllib2 import Request, urlopen
import math
import time

names={"temp":0.1,"test_pressure":0.2,"test_ph":0.3,"test_ec":0.4, "test_temp":0.5, "test_ph2":0.6, "test_temp1":0.7, "test_temp2":0.8, "ph":0.9, "ec":10 }
#pump1=temp, pump2=test_pressure, pump3=test_ph, pump4=test_ec, pump5=test_temp, pump6=test_ph2, pump7=test_temp1 ,pump8=test_temp2, pump9=ph, alerts=ec

i=1

while(i):
    for key,val in names.iteritems():
        test_value=math.sin(i)+val
        json1= {
            "data_point": {
              "name": key,
              "value": val,
              "timestamp": int(time.time())
            }
          }
        key=str(key)
        val=str(False)
        t=str(int(time.time()))
        json="{\"data_point\":{\"name\":\""+key+"\", \"value\":"+val+",\"timestamp\":"+t+"}}"
        print json
        headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Token token="91cde66f8744bddb93103e41e91e6016"'
        }
        request = Request('http://api.autoponics.com/data_points', data=json, headers=headers)
        response_body = urlopen(request).read()
        print response_body
    i+=0.05
    time.sleep(3)  


