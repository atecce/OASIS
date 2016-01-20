from urllib2 import Request, urlopen
import math
import GUI_global
import time
GUI_global.init_sensor_hash_table()
"""print GUI_global.sensor_hash_table
print "new SHit"
print type(GUI_global.sensor_hash_table["P3"]) is bool""" 
i=1
while (i):
    for key,val in GUI_global.sensor_hash_table.iteritems():
        json1= {
            "data_point": {
              "name": key,
              "value": GUI_global.sensor_hash_table[key].value,
              "timestamp": GUI_global.sensor_hash_table[key].timestamp
            }
          }
        key=str(key)
        value=str(GUI_global.sensor_hash_table[key].value)
        t=str(int(time.time())-(i*50))        
        json="{\"data_point\":{\"name\":\""+key+"\", \"value\":"+value+",\"timestamp\":"+t+"}}"
        print json
        headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Token token="91cde66f8744bddb93103e41e91e6016"'
        }
        #print json
        request = Request('http://api.autoponics.com/data_points', data=json, headers=headers)
        response_body = urlopen(request).read()
        print response_body
    print "done"
        
    i=0

