import zmq
import time
import json
#Initializing server as PAIR
port="5555"
context=zmq.Context();
socket_control=context.socket(zmq.PAIR);
socket_control.bind("tcp://*:%s" % port);

#Send message to client
def send_to_client(value):
    value=json.dumps(value);
    socket_control.send(value);
    return

#Thread which constantly recives messages from the client and
#queue them to the QMH
class VPD(threading.Thread):
    def __init__(global_event):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            msg=socket_control.recv();
            msg=json.loads(msg)
            #Queue here and keep going
        
    
    
