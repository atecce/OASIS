import Queue
import threading
import time
import json
import zmq
import global_var
import numpy
class Generic_Sensor_Struct():
    def __init__(self, timestamp, value,component):
        self.value = value
        self.timestamp = timestamp
        self.component=component
def Message_Queue(obj):
        BB1_msg_q.put(obj)
        return
BB1_msg_q=Queue.Queue() #Create global queue
#------------------------------------------------------------------------------------------#
"Messaging Queue for Sensor Data as server"
#Initializing server as PAIR
def init_messages():
    port="5565"
    context=zmq.Context();
    global socket_control
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
            
def HSST_update():
    global_var.hsst_hash[consumer.key]=consumer.value;
    return

#------------------------------------------------------------------------------------------#
def main():
        #BB1_msg_q=Queue.Queue() #Create global queue
        init_messages();
        thread1=Server_receive()
        thread1.start()
        global_var.init_sensor_hash_table()#Initialize sensor hash table
        x=Generic_Sensor_Struct(1,2,3)
        x.value=5;

        global_var.insert_sensor_hash("EC_1",x)
        a=global_var.sensor_hash_table["EC_1"]
        print a
        a=a[0];
        print a
        print a.value
        while True:
                print BB1_msg_q.get();
                time.sleep(5)


main()
