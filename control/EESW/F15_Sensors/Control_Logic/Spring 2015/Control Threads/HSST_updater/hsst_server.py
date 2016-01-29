import Queue
import threading
import time
import json
import zmq
import global_var

class Generic_Sensor_Struct():
    def __init__(self, timestamp, value,component):
        self.value = value
        self.timestamp = timestamp
        self.component=component
#------------------------------------------------------------------------------------------#
"Messaging Queue for Sensor Data as server"
#Initializing server as PAIR
def init_messages():
    port="5555"
    context=zmq.Context();
    global socket_control;
    socket_control=context.socket(zmq.PAIR);
    socket_control.bind("tcp://*:%s" % port);
    return

#Send message to client
def send_to_client(value):
    value=json.dumps(value);
    socket_control.send(value);
    return

#Thread which constantly recives messages from the client and
#queue them to the QMH
class Server_receive(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            msg=socket_control.recv();
            msg=json.loads(msg)
            Message_Queue(msg); #Enqueue Message

#------------------------------------------------------------------------------------------#
def main():
        BB1_msg_q=Queue.Queue() #Create global queue
        init_mesages();
        thread1=Server_receive()
        thread1.start()
        global_var.init_sesnor_hash_table()#Initialize sensor hash table
        x=Generic_sensor_struct(1,2,3)
        x.value=5;
        insert_sensor_hash("EC_1",x)
        a=global_var.sensor_hash_table["EC_1"]
        print a
        print a.value
        
            
