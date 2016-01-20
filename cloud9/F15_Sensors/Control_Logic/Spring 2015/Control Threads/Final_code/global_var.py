#Default Class for initialization
class Sensor():
        def __init__(self,value,timestamp):
            self.value=value
            self.timestamp=timestamp
            
class HSST():
    def __init__(self,case,key,value):
        self.case=case
        self.key=key
        self.value=value

class relay():
    def __init__(self,case,port_id,status):
        self.case=case
        self.port_id=port_id
        self.status=status  
        

#------------------------------------------------------------------------------------------#
"Initializes the hash map with the 10 readings of sensor objects arranged in a ring buffer"
#Sensor Hash Table
sensor_hash_table={}
def init_sensor_hash_table():
    sensor_hash_table['DO_1']=Sensor("555555","1")
    sensor_hash_table['EC_1']=Sensor("555555","1")
    sensor_hash_table['EC_2']=Sensor("555555","1")
    sensor_hash_table['TEMP_1']=Sensor("555555","1")  
    sensor_hash_table['TEMP_2']=Sensor("555555","1")    
    sensor_hash_table['TEMP_3']=Sensor("555555","1")
    sensor_hash_table['TEMP_4']=Sensor("555555","1") 
    sensor_hash_table['TEMP_5']=Sensor("555555","1")
    sensor_hash_table['LL_1']=Sensor("555555","1")  
    sensor_hash_table['LL_2']=Sensor("555555","1")    
    sensor_hash_table['LL_3']=Sensor("555555","1")	
    sensor_hash_table['LL_4']=Sensor("555555","1") 
    sensor_hash_table['LL_5']=Sensor("555555","1")  
    sensor_hash_table['LL_6']=Sensor("555555","1")
    sensor_hash_table['LL_7']=Sensor("555555","1")
    sensor_hash_table['FL_1']=Sensor("555555","1")
    sensor_hash_table['FL_2']=Sensor("555555","1") 
    sensor_hash_table['PH_1']=Sensor("555555","1")  
    sensor_hash_table['PH_2']=Sensor("555555","1")    
    sensor_hash_table['MTR_1']=Sensor("555555","1")	
    sensor_hash_table['MTR_2']=Sensor("555555","1") 
    sensor_hash_table['MTR_3']=Sensor("555555","1")  
    sensor_hash_table['MTR_4']=Sensor("555555","1")    
    sensor_hash_table['RHT_1']=Sensor("555555","1")
    sensor_hash_table['RHT_1_TEMP']=Sensor("555555","1")
    sensor_hash_table['RHT_2']=Sensor("555555","1")
    sensor_hash_table['RHT_2_TEMP']=Sensor("555555","1")
    sensor_hash_table['RHT_3']=Sensor("555555","1")
    sensor_hash_table['RHT_3_TEMP']=Sensor("555555","1")
    sensor_hash_table['PR_1']=Sensor("555555","1")    
    sensor_hash_table['PR_2']=Sensor("555555","1")
    sensor_hash_table['O2_1']=Sensor("555555","1")
    sensor_hash_table['O2_2']=Sensor("555555","1") 
    sensor_hash_table['CO2_1']=Sensor("555555","1")  
    sensor_hash_table['CO2_2']=Sensor("555555","1")    
    sensor_hash_table['PAR_1']=Sensor("555555","1")
    sensor_hash_table['PAR_2']=Sensor("555555","1")
    sensor_hash_table['P1']=Sensor("555555","1") #Pumps and solenoids are boolean objects
    sensor_hash_table['P2']=Sensor("555555","1")
    sensor_hash_table['P3']=Sensor("555555","1")
    sensor_hash_table['P4']=Sensor("555555","1")
    sensor_hash_table['P5']=Sensor("555555","1")
    sensor_hash_table['P8']=Sensor("555555","1")
    sensor_hash_table['M1']=Sensor("555555","1")
    sensor_hash_table['M2']=Sensor("555555","1")
    sensor_hash_table['P10']=Sensor("555555","1")
    sensor_hash_table['M9']=Sensor("555555","1")
    sensor_hash_table['P12']=Sensor("555555","1")
    sensor_hash_table['V3']=Sensor("555555","1")
    sensor_hash_table['M8']=Sensor("555555","1")
    sensor_hash_table['V4']=Sensor("555555","1")
    sensor_hash_table['P11']=Sensor("555555","1")
    sensor_hash_table['P7']=Sensor("555555","1")
    sensor_hash_table['F2']=Sensor("555555","1")
    sensor_hash_table['M6']=Sensor("555555","1")
    sensor_hash_table['M7']=Sensor("555555","1")
    sensor_hash_table['P6']=Sensor("555555","1")
    sensor_hash_table['P9']=Sensor("555555","1")
    sensor_hash_table['ST']=Sensor("555555","1")
    sensor_hash_table['M18']=Sensor("555555","1") #LED
    
    return


#------------------------------------------------------------------------------------------#
"""" Insert data into seonsor hash table """

"""def insert_sensor_hash(key,obj):
    sensor_hash_table[key]= np.roll(sensor_hash_table[key],1)
    sensor_hash_table[key][0]=obj"""
#------------------------------------------------------------------------------------------#
"------------------------------------------------------------------------------------------"
#HSST Hash Taable
hsst_hash = {} #Declare Hash table
def init_hsst_hash_table():
    
    alphabet_arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W']
    workbook = xlrd.open_workbook('dummy.xls')
    worksheet = workbook.sheet_by_name('Sheet1')
    num_rows = worksheet.nrows - 1
    num_cells = worksheet.ncols - 1
    curr_row = -1
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        # print 'Row:', curr_row
        curr_cell = -1
        while curr_cell < num_cells:
            curr_cell += 1
            # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
            cell_type = worksheet.cell_type(curr_row, curr_cell)
            cell_value = worksheet.cell_value(curr_row, curr_cell)
            key_label = alphabet_arr[curr_cell] + str(curr_row+1)
            hsst_hash[key_label] = cell_value
            #print key_label
            #print cell_value
    return
#------------------------------------------------------------------------------------------#
#Flags
watering_paused=False;
Moisture_Ready=False; # True when you get moisture sensor values from BBB2
