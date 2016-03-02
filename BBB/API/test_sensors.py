# need this for test sensors
from test_API import test_sensor, test_relative_humidity_and_air_temperature

# populate sensor suite
S = {
     # liquid tanks and plumbing		
     101: test_sensor(101, 1150, 1250),
     102: test_sensor(102,  5.5,    6),     
     103: test_sensor(103,   22,   24),
#     104:   I2C_sensor("do_probe_and_circuitry",   0x61),
     105: test_sensor(105,  2.5,   13), 
     106: test_sensor(106,  2.5,    6),
     107: test_sensor(107,  2.5,    6),
     108: test_sensor(108,  2.5,    6),
     109: test_sensor(109,  2.5,    6),
     110: test_sensor(110,  .23,  .47),
     111: test_sensor(111,  .23,  .47),
     112: test_sensor(112,  2.5,    6),

     # growth medium
     201: test_sensor(201,   15,   20), 
     202: test_sensor(202,   15,   20),
     203: test_sensor(203,   15,   20),
     205: test_sensor(205, 1150, 1250),
     206: test_sensor(206,  5.5,    6),
     208: test_sensor(208,   25,   50),
     209: test_sensor(209,   25,   50),
     210: test_sensor(210,  25,   50),
     211: test_sensor(211,  25,   50),

     # internal atmosphere
     301: test_relative_humidity_and_air_temperature(301),
     302: test_relative_humidity_and_air_temperature(302),
     303: test_sensor(303,   80,   84),
     304: test_sensor(304,   10,   25),
     305: test_sensor(305, 1000, 2000),
     306: test_sensor(306,  200,  250),

     # external environment
     401: test_relative_humidity_and_air_temperature(401),
     402: test_sensor(402,  80,  84),
     403: test_sensor(403, 200, 250)}
