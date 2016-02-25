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

if __debug__:
    pass    
else:
    import Adafruit_BBIO.UART as UART
    import Adafruit_BBIO.GPIO as GPIO
    import smbus
    import numpy as np

#sensor_hash_table={} #create sersor hash table
BB2_msg_q=Queue.Queue() #Create global queue

"Enqueue Function"
def Message_Enqueue(obj):
    BB2_msg_q.put(obj)
    return

#------------------------------------------------------------------------------------------#
#Gloabl Classes
    
#------------------------------------------------------------------------------------------#

"""Sensor Object structures"""

class Generic_Sensor_Struct():
    def __init__(self, timestamp, value,component):
        self.value = value
        self.timestamp = timestamp
        self.component=component

class RH_Temp_Struct():
    def __init__(self, timestamp, RH,Temp,component):
        self.RH = RH
        self.Temp = Temp
        self.timestamp = timestamp
        self.component=component
        
class Flow_Meter_Struct():
    def __init__(self,timestamp,x,y,z,component):
        self.x=x
        self.y=y
        self.z=z
        self.timestamp=timestamp
        self.component=component
        
class Camera_Struct():
    def __init__(self,timestamp,arr):
        self.arr=arr
        self.timestamp=timestamp


#------------------------------------------------------------------------------------------#
             
""" Thread data object classes """

class PWM_Data():
    def __init__(self, duty_cycle, freq, port,component):
        self.duty_cycle = duty_cycle
        self.freq = freq
        self.port = port
        self.component = component

"""ADC Data Class"""
class ADC_Data():
   def __init__(self, reading, port,component):
       self.reading = reading
       self.port = port
       self.component = component




class RH_Temp_Data():
    def __init__(self, reading_RH, reading_Temp, address, port,component):
        self.reading_RH = reading_RH
        self.reading_Temp = reading_Temp
        self.address = address
        self.port = port
        self.component = component
#------------------------------------------------------------------------------------------#
#Functions

#------------------------------------------------------------------------------------------#
#Network Classes
class HSST_element():
    def __init__(self, case, key, value):
        self.case=case
        self.key=key
        self.value=value

class relay():
    def __init__(self,case,port_id,status):
        self.case=case
        self.port_id=port_id
        self.status=status
#------------------------------------------------------------------------------------------#
#Sensor and pump message Queue

def init_clinet_messages:
    port="5555"
    context=zmq.Context();
    socket_client=context.socket(zmq.PAIR);
    socket_client.connect("tcp://localhost:%s" % port)
    return
#The only information we send here should be the VWC or VPD value
def client_send(msg):
    msg=pickle.dumps(msg);
    socket_client.send(msg);
#The only information we receive is to turn the relay on for a few pumps/solenoids
# This will also handle global pause and resume functions
class client_rcv(threading.Thread):
    def __init__(global_event):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            msg=socket_client.recv();
            msg=pickle.loads(msg)
            if (msg.case=="GPIO"):
                mech_ctrl.GPIO_set(msg.arg1,msg.arg2) #Set GPIO Pin as Required
            else if (msg.case=="global_pause"):
                global_pause()
            else if (msg.case=="gloabl_resume"):
                global_resume()
            
        return

#------------------------------------------------------------------------------------------#        
def init_clinet_hsst:
    port="5556"
    context_hsst=zmq.Context();
    socket_hsst=context_hsst.socket(zmq.PAIR);
    socket_hsst.connect("tcp://localhost:%s" % port)
    return

#The only information we send here is sensor Value to update HSST table packed as the
#HSST_element class
def hsst_send(msg):
    msg=pickle.dumps(msg);
    socket_hsst.send(msg);

#The will not be used and this thread should not be launched. Implemented for future expnasion
class hsst_rcv(threading.Thread):
    def __init__(global_event):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            msg=socket_hsst.recv();
            msg=pickle.loads(msg)
                        
        return
#------------------------------------------------------------------------------------------#
#Common classes and functions
"Build Case Structure i.e C switch statement equivalent"

class relay():
    def __init__(self,case,port_id,status):
        self.case=case
        self.port_id=port_id
        self.status=status  
    
"""def HSST_update(element):
        global_var.sensor_hash_table[element.key]=element.value
        return"""
    
class HSST_element():
    def __init__(self, case, key, value):
        self.case=case
        self.key=key
        self.value=value

#Default class to be used on all QMH. This has two arguemnts and a case selector        
class QMH_element():
    def __init__(self,case,arg1,arg2):
        self.case=case
        self.arg1=arg1
        self.arg2=arg2

def gloal_pause():
    global_event.event.clear();

def global_resume():
    global_event.event.set()
#------------------------------------------------------------------------------------------#
#Main Loop
def main():
    #Message Thread Init
    init_client_messages()
    sensor_thread_client=client_rcv()
    sensor_thread_client.start()
    #Hsst send Init
    init_client_hsst()
    #Setup GPIO Lines
    mech_ctrl.setup_GPIO_BB2();
    #Initialize Events
    global_event=threading.Event();
    global_event.event.set();
    # use global_event.event.clear() to stop or pause all control loops
    #This happens from GUI
    
    #Build Switch case using dictionary
    switch={"""Update all cases here as a dictionary"""}

    #Build QMH

    while True:
        consumer=BB2_msg_q.get
        try:
            switch[consumer.case]();
        except NameError:
            pass
            #Use this as the default case
    
