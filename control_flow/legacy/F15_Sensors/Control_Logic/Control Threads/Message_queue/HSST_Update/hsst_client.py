
import zmq
import time
import cPickle as pickle
#import pickle
import threading
#initializing client as PAIR
port="5513"

context=zmq.Context();
socket_client=context.socket(zmq.PAIR);
socket_client.connect("tcp://localhost:%s" % port)

#Send messages to server
def client_send(msg):
    msg=pickle.dumps(msg);
    socket_client.send(msg);
    return

#Receive messages from server and handle it
class VPD(threading.Thread):
    def __init__(global_event):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            msg=socket_client.recv();
            msg=pickle.loads(msg)
            #Queue here and keep going

class HSST_element():
    def __init__(self, case, key, value):
        self.case=case
        self.key=key
        self.value=value

class Generic_Sensor_Struct():
    def __init__(self, timestamp, value,component):
        self.value = value
        self.timestamp = timestamp
        self.component=component
def main():
    element=Generic_Sensor_Struct("time","value","component")
    print type(element)
    #element=pickle.dumps(element)
    msg=HSST_element("update_HSST","EC_1",element)
    print type(msg)
    client_send(msg);
main()
