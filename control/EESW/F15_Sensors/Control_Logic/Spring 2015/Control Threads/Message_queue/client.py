import zmq
import time
import json
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

    
#Receive messages from server and handle it
class VPD(threading.Thread):
    def __init__(global_event):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            msg=socket_client.recv();
            msg=json.loads(msg)
            #Queue here and keep going
            
