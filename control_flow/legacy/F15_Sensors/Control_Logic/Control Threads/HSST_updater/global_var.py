import numpy

#------------------------------------------------------------------------------------------#
"Initializes the hash map with the 10 readings of sensor objects arranged in a ring buffer"
#Sensor Hash Table
sensor_hash_table={}
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

