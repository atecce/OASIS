import Queue
import threading
import numpy as np
import time
import datetime

bb1_msg_q = Queue.Queue() #create the global queue
sensor_hash_table={}


#------------------------------------------------------------------------------------------# 
##class Message_Queuing(threading.Thread):
##    def __init__(self,obj):
##        threading.Thread.__init__(self)
##        self.obj=obj
##
##    def run(self):
##        bb1_msg_q.put(self.obj)
##        "queued"

def Message_Queuing(obj):
    bb1_msg_q.put(obj)
    


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


class I2C_Data():
    def __init__(self, reading, address, port,component):
        self.reading = reading
        self.address = address
        self.port = port
        self.component = component

class RH_Temp_Data():
    def __init__(self, reading_RH, reading_Temp, address, port,component):
        self.reading_RH = reading_RH
        self.reading_Temp = reading_Temp
        self.address = address
        self.port = port
        self.component = component

class UART_Data():
    def __init__(self, reading, port_RX, port_TX,component):
        self.reading = reading
        self.port_RX = port_RX
        self.port_TX = port_TX
        self.component = component
#------------------------------------------------------------------------------------------#       
""" Control Threads Code"""

class PWM_Control_Thread_Code(threading.Thread):
    def __init__(self,duty_cycle,freq,port,component):
        threading.Thread.__init__(self)
        self.duty_cycle=duty_cycle
        self.freq=freq
        self.port=port
        self.component=component
        

    def run(self):
        a=  PWM_Data(self.duty_cycle,self.freq,self.port,self.component)
        thread1 = Message_Queuing(a)	
        thread1.start()




#------------------------------------------------------------------------------------------#
""" Sensor Thread Code """

class CO21_Sensor_Thread_Code(threading.Thread):
    def __init__(self,component):
        self.component="CO21"
        threading.Thread.__init__(self)

    def run(self):
        while(1):
            CO21_value=1.1   #this is calculated by the sensor code
            CO21_Object=Generic_Sensor_Struct(time.time(),CO21_value,'CO21');
            Message_Queuing(CO21_Object)
            time.sleep(1)

        
class O21_Sensor_Thread_Code(threading.Thread):
    def __init__(self,component):
        self.component="O21"
        threading.Thread.__init__(self)

    def run(self):
        while(1):
            O21_value=2.1   #this is calculated by the sensor code
            O21_Object=Generic_Sensor_Struct(time.time(),O21_value,'O21');
            Message_Queuing(O21_Object)
            time.sleep(1)


class O22_Sensor_Thread_Code(threading.Thread):
    def __init__(self,component):
        self.component="O22"
        threading.Thread.__init__(self)

    def run(self):
        while(1):
            O22_value=2.1   #this is calculated by the sensor code
            O22_Object=Generic_Sensor_Struct(time.time(),O22_value,'O22');
            Message_Queuing(O22_Object)
            time.sleep(1)


        
#------------------------------------------------------------------------------------------#
"Initializes the hash map with the 10 readings of sensor objects arranged in a ring buffer"

def init_sensor_hash_table():
    sensor_hash_table['EC1']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['EC2']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['TEMP1']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['TEMP2']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['TEMP3']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['TEMP4']=np.arange(0,10,1, dtype=np.object) 
    sensor_hash_table['TEMP5']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['LL1']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['LL2']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['LL3']=np.arange(0,10,1, dtype=np.object)	
    sensor_hash_table['LL4']=np.arange(0,10,1, dtype=np.object) 
    sensor_hash_table['LL5']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['LL6']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['FL1']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['FL2']=np.arange(0,10,1, dtype=np.object) 
    sensor_hash_table['PH1']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['PH2']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['MTR1']=np.arange(0,10,1, dtype=np.object)	
    sensor_hash_table['MTR2']=np.arange(0,10,1, dtype=np.object) 
    sensor_hash_table['MTR3']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['MTR4']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['RHT1']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['RHT2']=np.arange(0,10,1, dtype=np.object) 
    sensor_hash_table['RHT3']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['PR1']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['PR2']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['O21']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['O22']=np.arange(0,10,1, dtype=np.object) 
    sensor_hash_table['CO21']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['CO22']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['PAR1']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['PAR2']=np.arange(0,10,1, dtype=np.object)
    #sensor_hash_table['LL7']=np.arange(0,10,1, dtype=np.object)

#------------------------------------------------------------------------------------------#
"""" Insert data into hash table """

def insert_data(key,obj):
    sensor_hash_table[key]= np.roll(sensor_hash_table[key],1)
    sensor_hash_table[key][0]=obj
    
#------------------------------------------------------------------------------------------#
"""Main loop"""

def main():

    init_sensor_hash_table()
    co2thread=CO21_Sensor_Thread_Code("CO21")
    co2thread.start()
    o2thread=O21_Sensor_Thread_Code("O21")
    o2thread.start()
   
    while(1):
        print "in while"
        x=bb1_msg_q.get()
        print x.component
        print x.value
        print x.timestamp
            



main()
#try except

"""try:
    some_function()
except Exception:"""
# if the cause of exception doesnot stop if we restart the thread and if error keeps comming kill it
# dependent variables are reset when a thread is restarted
#supervisor tool in linux
    



    
    
