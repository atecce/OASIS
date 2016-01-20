import smbus #import smbus library
import time

def ec_read():
    flag=0
    while True:

        try:
            slave_add=0x64;
            #print" in try block1"
            flag=flag+1;
            #print flag
            bus=smbus.SMBus(1) #assign an object to the SMBus class and mention the interface number
            time.sleep(3)
            bus.write_byte(slave_add,0x52) #R
            time.sleep(3)
            results=bus.read_i2c_block_data(slave_add,0x52) #read cal info
            time.sleep(3)
            #print results
            for index, item in enumerate(results):
                if item == 0:
                       end_val = index
                       break
            results = results[1:end_val]
            results_string = ''.join(chr(i) for i in results)
           # #print" in main try"
           # #print results_string



        except Exception:
            if flag >2:
                print"false"
                return "False"
            else:
                continue;

        #print results_string
        return float(results_string)

ec_read()
