import Queue
import threading
import numpy as np
import time
import datetime
import serial
import time
import struct 
if __debug__:
    pass    
else:
    import Adafruit_BBIO.UART as UART
    import smbus




bb1_msg_q = Queue.Queue() #create the global queue
sensor_hash_table={}


#------------------------------------------------------------------------------------------# 
class Message_Queuing(threading.Thread):
    def __init__(self,obj):
        threading.Thread.__init__(self)
        self.obj=obj

    def run(self):
        bb1_msg_q.put(self.obj)
        "queued"

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

class CO2_Sensor_Thread(threading.Thread):
    def __init__(self,component,port_id):
        self.component=component
        if __debug__:
            pass    
        else:
            UART.setup(port_id)
        threading.Thread.__init__(self)

    def run(self):
        while(1):
            if __debug__:
                CO2_value=1.1   #simulated value for debugging   
            else:
                pass            #here goes the Co2 sensor code
      
            CO2_Object=Generic_Sensor_Struct(time.time(),CO2_value,self.component);
            Message_Queuing(CO2_Object)
            time.sleep(1)

        
"""EC Sensor Thread"""
class EC_Sensor_Thread(threading.Thread):
    def __init__(self,component,slave_address):
        self.component=component
        if __debug__:
            pass    
        else:
            pass # Enter any init code here if necessary
        threading.Thread.__init__(self)

    def run(self):
        while(1):
            if __debug__:
                EC_value=1.1   #simulated value for debugging   
            else:
                pass            #here goes the EC sensor code
      
            EC_Object=Generic_Sensor_Struct(time.time(),EC_value,self.component);
            Message_Queuing(EC_Object)
            time.sleep(1)

"""PH Sensors"""
class PH_Sensor_Thread(threading.Thread):
    def __init__(self,component,slave_address):
        self.component=component
        if __debug__:
            pass    
        else:
            pass # Enter any init code here if necessary
        threading.Thread.__init__(self)

    def run(self):
        while(1):
            if __debug__:
                PH_value=6.5   #simulated value for debugging   
            else:
                pass            #here goes the PH sensor code
      
            PH_Object=Generic_Sensor_Struct(time.time(),PH_value,self.component);
            Message_Queuing(PH_Object)
            time.sleep(1)
"""DO Sensor"""
class DO_Sensor_Thread(threading.Thread):
    def __init__(self,component,slave_address):
        self.component=component
        if __debug__:
            pass    
        else:
            pass # Enter any init code here if necessary
        threading.Thread.__init__(self)

    def run(self):
        while(1):
            if __debug__:
                DO_value=35   #simulated value for debugging   
            else:
                pass            #here goes the DO sensor code
      
            DO_Object=Generic_Sensor_Struct(time.time(),DO_value,self.component);
            Message_Queuing(DO_Object)
            time.sleep(1)
            
"""Moisture Sensor"""
class MTR_Sensor_Thread(threading.Thread):
    def __init__(self,component,port_id):
        self.component=component
        if __debug__:
            pass    
        else:
            pass # Enter any init code here if necessary
        threading.Thread.__init__(self)

    def run(self):
        while(1):
            if __debug__:
                MTR_value=67   #simulated value for debugging   
            else:
                pass            #here goes the DO sensor code
      
            MTR_Object=Generic_Sensor_Struct(time.time(),MTR_value,self.component);
            Message_Queuing(MTR_Object)
            time.sleep(1)
        
#------------------------------------------------------------------------------------------#
"Initializes the hash map with the 10 readings of sensor objects arranged in a ring buffer"

def init_sensor_hash_table():
    sensor_hash_table['EC_1']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['EC_2']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['TEMP_1']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['TEMP_2']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['TEMP_3']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['TEMP_4']=np.arange(0,10,1, dtype=np.object) 
    sensor_hash_table['TEMP_5']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['LL_1']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['LL_2']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['LL_3']=np.arange(0,10,1, dtype=np.object)	
    sensor_hash_table['LL_4']=np.arange(0,10,1, dtype=np.object) 
    sensor_hash_table['LL_5']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['LL_6']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['FL_1']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['FL_2']=np.arange(0,10,1, dtype=np.object) 
    sensor_hash_table['PH_1']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['PH_2']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['MTR_1']=np.arange(0,10,1, dtype=np.object)	
    sensor_hash_table['MTR_2']=np.arange(0,10,1, dtype=np.object) 
    sensor_hash_table['MTR_3']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['MTR_4']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['RHT_1']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['RHT_2']=np.arange(0,10,1, dtype=np.object) 
    sensor_hash_table['RHT_3']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['PR_1']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['PR_2']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['O2_1']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['O2_2']=np.arange(0,10,1, dtype=np.object) 
    sensor_hash_table['CO2_1']=np.arange(0,10,1, dtype=np.object)  
    sensor_hash_table['CO2_2']=np.arange(0,10,1, dtype=np.object)    
    sensor_hash_table['PAR_1']=np.arange(0,10,1, dtype=np.object)
    sensor_hash_table['PAR_2']=np.arange(0,10,1, dtype=np.object)
    #sensor_hash_table['LL7']=np.arange(0,10,1, dtype=np.object)
"HSST Hash table"

#------------------------------------------------------------------------------------------#
def init_sensor_threads():
    
    CO2_1_Thread=CO2_Sensor_Thread("CO2_1","UART1")
    CO2_1_Thread.start()
    CO2_2_Thread=CO2_Sensor_Thread("CO2_2","UART2")
    CO2_2_Thread.start()
    EC_1_Thread=EC_Sensor_Thread("EC_1","0x64")
    EC_1_Thread.start()
    PH_1_Thread=PH_Sensor_Thread("PH_1","0x63")
    PH_1_Thread.start()
    DO_1_Thread=PH_Sensor_Thread("DO_1","0x61")
    DO_1_Thread.start()
    MTR_1_Thread=MTR_Sensor_Thread("MTR_1","P1.7")
    MTR_1_Thread.start()
#------------------------------------------------------------------------------------------#
"""" Insert data into hash table """

def insert_data(key,obj):
    sensor_hash_table[key]= np.roll(sensor_hash_table[key],1)
    sensor_hash_table[key][0]=obj
    
#------------------------------------------------------------------------------------------#

"""Main loop"""

def main():
    init_sensor_hash_table()
    init_sensor_threads()

   
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
    
"Mechanical Components control library"



    
    
