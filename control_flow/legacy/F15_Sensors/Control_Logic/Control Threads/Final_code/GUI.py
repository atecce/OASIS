import time
import global_var
import threading
from urllib2 import Request, urlopen
import math

#Will send the sensor hash table to GUI
class GUI_update(threading.Thread):
    def __init__(self):
        threading.Thread. __init__(self)

    def run(self):
        while True:
            
            for key,val in global_var.sensor_hash_table.iteritems():
                try:
                    json1= {
                        "data_point": {
                          "name": key,
                          "value": global_var.sensor_hash_table[key].value,
                          "timestamp": global_var.sensor_hash_table[key].timestamp
                        }
                      }
                    key=str(key)
                    value=str(global_var.sensor_hash_table[key].value)
                    t=str(global_var.sensor_hash_table[key].timestamp)        
                    json="{\"data_point\":{\"name\":\""+key+"\", \"value\":"+value+",\"timestamp\":"+t+"}}"
                    #print json
                    headers = {
                      'Content-Type': 'application/json',
                      'Authorization': 'Token token="91cde66f8744bddb93103e41e91e6016"'
                    }
                    request = Request('http://api.autoponics.com/data_points', data=json, headers=headers)
                    response_body = urlopen(request).read()
                    #print response_body
                except Exception:
                    pass # do nothing when expception comes and keep going
            #print "done"
            #break
            time.sleep(180)
"""#TEST CODE 
def main():
    start_time = time.time()
    global_var.init_sensor_hash_table()
    thread1=GUI_update()
    thread1.start()
    thread1.join()
    print("--- %s seconds ---" % (time.time() - start_time))
    print "done"
    
main()"""
