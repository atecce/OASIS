
import Queue
import threading
import time
import json
import zmq
import global_var
import numpy
import cPickle as pickle
#import pickle

class Generic_Sensor_Struct():
        def __init__(self,case,key,value):
                self.case=case
                self.key=key
                self.value=value
class HSST_element():
        def __init__(self,case,key,value):
                self.case=case
                self.key=key
                self.value=value

def Message_Queue(obj):
        BB1_msg_q.put(obj)
        return
#------------------------------------------------------------------------------------------#
"Messaging Queue for Sensor Data as server"
#Initializing server as PAIR
def init_messages():
    port="5513"
    context=zmq.Context();
    global socket_control
    socket_control=context.socket(zmq.PAIR);
    socket_control.bind("tcp://*:%s" % port);
    return

#Send message to client
def send_to_client(value):
    value=pickle.dumps(value);
    socket_control.send(value);
    return



#Thread which constantly recives messages from the client and
#queue them to the QMH
class Server_receive(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
#class HSST_element():
#       def __init__(self,case,key,value):
#               self.case=case
#               self.key=key
#               self.value=value
        x=HSST_element(1,2,3)
        while True:
            msg=socket_control.recv();
            print msg
            msg=pickle.loads(msg)
            print msg
            Message_Queue(msg); #Enqueue Message



            
def HSST_update():
        print "we HEre"
        print global_var.sensor_hash_table[consumer.key]
        global_var.sensor_hash_table[consumer.key]=consumer.value
        print global_var.sensor_hash_table[consumer.key]
        return

#def HSST_element():
#       def __init__(self, case, key, value):
#               self.case=case
#               self.key=key
#               self.value=value
#------------------------------------------------------------------------------------------#
def main():
        global BB1_msg_q
        global consumer
        BB1_msg_q=Queue.Queue() #Create global queue
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
        #while True:
        #       print BB1_msg_q.get();
        #       time.sleep(5)
        switch={"update_HSST":HSST_update}
        while True:
                consumer=BB1_msg_q.get()
                print consumer.case
                switch[consumer.case]();
        return

main()
