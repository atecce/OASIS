import Queue
import threading
import time
import datetime
import serial
import json
import zmq
import mech_ctrl
import global_var
import cPickle as pickle
import Adafruit_BBIO.UART as UART
import Adafruit_BBIO.GPIO as GPIO
import smbus
import numpy as np
import Sensors
    


#sensor_hash_table={} #create sersor hash table
BB1_msg_q=Queue.Queue() #Create global queue

"Enqueue Function"
def Message_Queue(obj):
    BB1_msg_q.put(obj)
    return
#------------------------------------------------------------------------------------------#
#Global Classes
    
#------------------------------------------------------------------------------------------#

"""Sensor Object structures"""
       
class Camera_Struct():
    def __init__(self,timestamp,arr):
        self.arr=arr
        self.timestamp=timestamp



#------------------------------------------------------------------------------------------#
        
"Messaging Queue for Sensor Data as server"
#Initializing server as PAIR
def init_messages():
    port="5555"
    context=zmq.Context();
    global socket_control
    socket_control=context.socket(zmq.PAIR);
    socket_control.bind("tcp://*:%s" % port);
    return

#The only data we send is to turn on and off a few gpio lines on BBB2 and global pause and resume
def send_to_client(value):
    value=pickle.dumps(value);
    socket_control.send(value);
    return


#The only data we receive is the VPD or VWC value from the client or BBB2
#This enques to the main but is absolutely unnecessary and can be handled diferently
class server_receive(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            msg=socket_control.recv();
            msg=pickle.loads(msg)
            Message_Queue(msg); #Enqueue Message

#------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------#
"Message Queue to update HSST Table"
def init_HSST_messages():
    port="5556"
    context_HSST=zmq.Context();
    global socket_HSST
    socket_HSST=context_HSST.socket(zmq.PAIR);
    socket_HSST.bind("tcp://*:%s" % port);
    return

#This function should never be used as the HSST table only resides on BBB1 but this is
#left exposed for future expnasion
def send_HSST_message(value):
    value=pickle.dumps(value);
    socket_HSST.send(value);
    return

#Thread receives messages from client (BB2) and updates the HSST table 
class rcv_HSST_message(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            msg=socket_HSST.recv();
            msg=pickle.loads(msg)
            #Update hsst_hash table in global_var module
            gloabl_var.hsst_hash[msg.key]=msg.value

#------------------------------------------------------------------------------------------#


#Start Main loop
"Build Case Structure i.e C switch statement equivalent"
def relay_control():
    port_id=consumer.port_id;
    status=consumer.status;
    mech_ctrl.GPIO_set(port_id,status)
    return


    
"""def HSST_update(element):
        global_var.sensor_hash_table[element.key]=element.value
        return"""

#Default class to be used on all QMH. This has two arguemnts and a case selector
#This can also be used in the client sensor network queue
class QMH_element():
    def __init__(self,case,arg1,arg2):
        self.case=case
        self.arg1=arg1
        self.arg2=arg2

    

def main():
    
    tp_val=Sensors.tp_read()
    mech_ctrl.setup_GPIO_BB1()
    print "Pressure: %.2f hPa" % (tp_val/ 100.0)
    #print "Temperature: %.2f C" % temp
    
    global consumer #make consumer global

    #Init IPC threads
    """init_messages();
    init_HSST_messages();
    message_control_thread=server_receive(); # launch Receive thread
    message_control_thread.start();
    hsst_thread=rcv_HSST_message(); #launch hsst_rcv thread
    hsst_thread.start()"""
    #Setup GPIO


"""
    ec_val=Sensors.ec_read()
    print "EC value" + ec_val
    do_val=Sensors.do_read()
    print "DO value" + do_val
    ph_val=Sensors.ph_read()
    print "pH value" + ph_val
    O2_val=Sensors.O2_read()
    print "O2 value" + O2_val
    CO2_val=Sensors.CO2_read()
    print "CO2 value" + CO2_val
    par_val=Sensors.PAR_read()
    print "PAR value" + par_val

    """

 
    


        
main()
