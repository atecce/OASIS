#Default Class for initialization
class init_sensor():
    def __init__(self, value, timestamp):
        self.value=value;
        self.timestamp=timestamp

#------------------------------------------------------------------------------------------#
"Initializes the hash map with the 10 readings of sensor objects arranged in a ring buffer"
#Sensor Hash Table
sensor_hash_table={}
def init_sensor_hash_table():
    sensor_hash_table['DO_1']=init_sensor("555555","1")
    sensor_hash_table['EC_1']=init_sensor("555555","1")
    sensor_hash_table['EC_2']=init_sensor("555555","1")
    sensor_hash_table['TEMP_1']=init_sensor("555555","1")  
    sensor_hash_table['TEMP_2']=init_sensor("555555","1")    
    sensor_hash_table['TEMP_3']=init_sensor("555555","1")
    sensor_hash_table['TEMP_4']=init_sensor("555555","1") 
    sensor_hash_table['TEMP_5']=init_sensor("555555","1")
    sensor_hash_table['LL_1']=init_sensor("555555","1")  
    sensor_hash_table['LL_2']=init_sensor("555555","1")    
    sensor_hash_table['LL_3']=init_sensor("555555","1")	
    sensor_hash_table['LL_4']=init_sensor("555555","1") 
    sensor_hash_table['LL_5']=init_sensor("555555","1")  
    sensor_hash_table['LL_6']=init_sensor("555555","1")
    sensor_hash_table['LL_7']=init_sensor("555555","1")
    sensor_hash_table['FL_1']=init_sensor("555555","1")
    sensor_hash_table['FL_2']=init_sensor("555555","1") 
    sensor_hash_table['PH_1']=init_sensor("555555","1")  
    sensor_hash_table['PH_2']=init_sensor("555555","1")    
    sensor_hash_table['MTR_1']=init_sensor("555555","1")	
    sensor_hash_table['MTR_2']=init_sensor("555555","1") 
    sensor_hash_table['MTR_3']=init_sensor("555555","1")  
    sensor_hash_table['MTR_4']=init_sensor("555555","1")    
    sensor_hash_table['RHT_1']=init_sensor("555555","1")
    sensor_hash_table['RHT_1_TEMP']=init_sensor("555555","1")
    sensor_hash_table['RHT_2']=init_sensor("555555","1")
    sensor_hash_table['RHT_2_TEMP']=init_sensor("555555","1")
    sensor_hash_table['RHT_3']=init_sensor("555555","1")
    sensor_hash_table['RHT_3_TEMP']=init_sensor("555555","1")
    sensor_hash_table['PR_1']=init_sensor("555555","1")    
    sensor_hash_table['PR_2']=init_sensor("555555","1")
    sensor_hash_table['O2_1']=init_sensor("555555","1")
    sensor_hash_table['O2_2']=init_sensor("555555","1") 
    sensor_hash_table['CO2_1']=init_sensor("555555","1")  
    sensor_hash_table['CO2_2']=init_sensor("555555","1")    
    sensor_hash_table['PAR_1']=init_sensor("555555","1")
    sensor_hash_table['PAR_2']=init_sensor("555555","1")
    sensor_hash_table['P1']=init_sensor("555555","1") #Pumps and solenoids are boolean objects
    sensor_hash_table['P2']=init_sensor("555555","1")
    sensor_hash_table['P3']=init_sensor("555555","1")
    sensor_hash_table['P4']=init_sensor("555555","1")
    sensor_hash_table['P5']=init_sensor("555555","1")
    sensor_hash_table['P8']=init_sensor("555555","1")
    sensor_hash_table['M1']=init_sensor("555555","1")
    sensor_hash_table['M2']=init_sensor("555555","1")
    sensor_hash_table['P10']=init_sensor("555555","1")
    sensor_hash_table['M9']=init_sensor("555555","1")
    sensor_hash_table['P12']=init_sensor("555555","1")
    sensor_hash_table['V3']=init_sensor("555555","1")
    sensor_hash_table['M8']=init_sensor("555555","1")
    sensor_hash_table['V4']=init_sensor("555555","1")
    sensor_hash_table['P11']=init_sensor("555555","1")
    sensor_hash_table['P7']=init_sensor("555555","1")
    sensor_hash_table['F2']=init_sensor("555555","1")
    sensor_hash_table['M6']=init_sensor("555555","1")
    sensor_hash_table['M7']=init_sensor("555555","1")
    sensor_hash_table['P6']=init_sensor("555555","1")
    sensor_hash_table['P9']=init_sensor("555555","1")
    sensor_hash_table['ST']=init_sensor("555555","1")   
    
    return


#------------------------------------------------------------------------------------------#
"""" Insert data into seonsor hash table """

def insert_sensor_hash(key,obj):
    sensor_hash_table[key]= np.roll(sensor_hash_table[key],1)
    sensor_hash_table[key][0]=obj
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
