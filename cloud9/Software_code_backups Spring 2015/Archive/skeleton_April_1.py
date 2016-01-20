import Queue
import threading


bb1_msg_q = Queue.Queue()



class Message_Queuing(threading.Thread):
    def __init__(self,obj):
        threading.Thread.__init__(self)
        self.obj=obj

    def run(self):
        bb1_msg_q.put(self.obj)

                
""" Thread data object classes """

class PWM_Data():
    def __init__(self, duty_cycle, freq, port,component):
        self.duty_cycle = duty_cycle
        self.freq = freq
        self.port = port
        self.component = component


""" Thread code classes"""

class LED_Control_Thread_Code(threading.Thread):
    def __init__(self,duty_cycle,freq,port):
        threading.Thread.__init__(self)
        print  "in thread init"
        self.duty_cycle=duty_cycle
        self.freq=freq
        self.port=port
        

    def run(self):
        print "pwm data before"
        a=  PWM_Data(self.duty_cycle,self.freq,self.port,"LED")
        thread1 = Message_Queuing(a)	
        thread1.start()
        print "led thread launcehd"
        #ctr=ctr+1
        #thread1.join()


def main():

    led=LED_Control_Thread_Code(50,1000,"p1.7")
    led.start()
    while(1):
        #print "we here"
        while not bb1_msg_q.empty():
            x=bb1_msg_q.get()
            print " This is interation :",
            if (x.component=="LED"):
                print "Port is :",
                print x.port
                print "duty cycle is :",
                print x.duty_cycle
                print "frequency is :",
                print x.freq
                led=LED_Control_Thread_Code(50,1000,"p1.7")
                led.start()
                led.join()

    


main()
