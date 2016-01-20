import Queue
import threading
import numpy as np

bb1_msg_q = Queue.Queue() #create the global queue
sensor_hash_table={}

class Message_Queuing(threading.Thread):
    def __init__(self,obj):
        threading.Thread.__init__(self)
        self.obj=obj

    def run(self):
        bb1_msg_q.put(self.obj)


#------------------------------------------------------------------------------------------#        
"""Sensor Object structures"""

class Generic_Sensor_Struct():
    def __init__(self, timestamp, value):
        self.value = value
        self.timestamp = timestamp

class RH_Temp_Struct():
    def __init__(self, timestamp, RH,Temp):
        self.RH = RH
        self.Temp = Temp
        self.timestamp = timestamp

class Flow_Meter_Struct():
    def __init__(self,timestamp,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.timestamp=timestamp
        
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
       self.component = "ADC_data"
#------------------------------------------------------------------------------------------#       
""" Thread code classes"""

class PWM_Control_Thread_Code(threading.Thread):
    def __init__(self,duty_cycle,freq,port,component):
        threading.Thread.__init__(self)
        print  "in thread init"
        self.duty_cycle=duty_cycle
        self.freq=freq
        self.port=port
        self.component=component
        

    def run(self):
        print "pwm data before"
        a=  PWM_Data(self.duty_cycle,self.freq,self.port,self.component)
        thread1 = Message_Queuing(a)	
        thread1.start()
        print "led thread launcehd"
        #ctr=ctr+1
        #thread1.join()


class ADC_Control_Thread_Code(threading.Thread):
    def __init__(self,reading,port,component):
        self.reading=reading
        self.port=port
        self.component=component
        

    def run(self):
        print "pwm data before"
        a=  ADC_Data(self.reading,self.port,self.component)
        thread1 = Message_Queuing(a)	
        thread1.start()
        print "led thread launched"
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


"""" Insert data into hash table """

def insert_data(key,obj):
    sensor_hash_table[key]= np.roll(sensor_hash_table[key],1)
    sensor_hash_table[key][0]=obj

"""Main loop"""

def main():

    init_sensor_hash_table()
    obj1=Generic_Sensor_Struct("time=now",1.3890)
    obj2=Generic_Sensor_Struct("time=now",7.9839)



main()





    
    
