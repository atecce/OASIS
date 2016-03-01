# need this for test sensors
from test_API import test_sensor, test_RHTemp

# populate sensor suite
S = {
     # liquid tanks and plumbing		
     101: test_sensor(1150, 1250),
     102: test_sensor( 5.5,    6),     
     103: test_sensor(  22,   24),
#     104:   I2C_sensor("do_probe_and_circuitry",   0x61),
     105: test_sensor( 2.5,   13), 
     106: test_sensor( 2.5,    6),
     107: test_sensor( 2.5,    6),
     108: test_sensor( 2.5,    6),
     109: test_sensor( 2.5,    6),
     110: test_sensor( .23,  .47),
     111: test_sensor( .23,  .47),
     112: test_sensor( 2.5,    6),

     # growth medium
     201: test_sensor(  15,   20), 
     202: test_sensor(  15,   20),
     203: test_sensor(  15,   20),
     205: test_sensor(1150, 1250),
     206: test_sensor( 5.5,    6),
     208: test_sensor(  25,   50),
     209: test_sensor(  25,   50),
     210: test_sensor(  25,   50),
     211: test_sensor(  25,   50),

     # internal atmosphere
     301: test_RHTemp(),
     302: test_RHTemp(),
     303: test_sensor(  80,   84),
     304: test_sensor(  10,   25),
     305: test_sensor(1000, 2000),
     306: test_sensor( 200,  250),

     # external environment
     401: test_RHTemp(),
     402: test_sensor( 80,  84),
     403: test_sensor(200, 250)}
