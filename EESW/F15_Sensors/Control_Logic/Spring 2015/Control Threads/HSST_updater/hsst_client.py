import zmq
import time
import json

class HSST_element():
    def __init__(self, case, key, value):
        self.case=case
        self.key=key
        self.value=value
 
#initializing client as PAIR
port="5566"
context=zmq.Context();
socket_client=context.socket(zmq.PAIR);
socket_client.connect("tcp://localhost:%s" % port)

#Send messages to server
def client_send(msg):
    msg=json.dumps(msg);
    socket_client.send(msg);
    return
