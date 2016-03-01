# API Documentation

To use the API you must have the API folder in your directory.

## Test API

### Test sensors

In order to import the test sensors type:

```python 
from API.test_sensors import S
```

This gives you access to the following dictionary:

```python 
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
     301: test_relative_humidity_and_temperature(),
     302: test_relative_humidity_and_temperature(),
     303: test_sensor(  80,   84),
     304: test_sensor(  10,   25),
     305: test_sensor(1000, 2000),
     306: test_sensor( 200,  250),

     # external environment
     401: test_relative_humidity_and_temperature(),
     402: test_sensor( 80,  84),
     403: test_sensor(200, 250)}
```

DO sensor is a special case (like RHTemp). It has no upper bound. Will work on it later.

If you want a handy way to find out which SysID corresponds to which kind of sensor, you can use the following:

```python
from API.conversions import sensor_type
```

This gives you access to the following dictionary:

```python
# returns the sensor type when given SysID
sensor_type = {

	101: "electrical conductivity",
	102: "pH",
	103: "liquid temperature",
	104: "dissolved oxygen",
	105: "liquid level", 
	106: "liquid level",
	107: "liquid level",
	108: "liquid level",
	109: "liquid level",
	110: "flow meter",
	111: "flow meter",
	112: "liquid level",

	201: "soil temperature", 
	202: "soil temperature",
	203: "soil temperature",
	205: "electrical conductivity",
	206: "pH",
	208: "moisture",
	209: "moisture",
	210: "moisture",
	211: "moisture",

	301: "relative humidity and air temperature",
	302: "relative humidity and air temperature",
	303: "total pressure",
	304: "oxygen",
	305: "carbon dioxide",
	306: "photosynthetically active radiation",

	401: "relative humidity and air temperature",
	402: "total pressure",
	403: "photosynthetically active radiation"}
```

There is also another notation in use, which is easier for dealing with the individual sensors and not worrying about the algorithms. These dictionaries give the one-to-one relationship between the SysID and the senseID (as I will call it).

```python
from API.conversions import senseIDtoSysID, SysIDtosenseID
```

And they look like this:

```python
# returns the SysID when given senseID
senseIDtoSysID = {

	'EC1': 101,
	'EC2': 205,

	'temp1': 103,
	'temp2': 201,
	'temp3': 202,
	'temp4': 203,

	'DO': 104,

	'LL1': 105,
	'LL2': 106,
	'LL3': 107,
	'LL4': 108,
	'LL5': 109,
	'LL6': 112,

	'flow_meter1': 110,
	'flow_meter2': 111,

	'pH1': 102,
	'pH2': 206,

	'MO1': 208,
	'MO2': 209,
	'MO3': 210,
	'MO4': 211,

	'RHT1': 301,
	'RHT2': 302,
	'RHT3': 401,

	'TP1': 303,
	'TP2': 402,

	'O2': 304,

	'CO2': 305,

	'PAR1': 306,
	'PAR2': 403}

# returns the senseID when given SysID
sensor_type = {

	101: "electrical conductivity",
	102: "pH",
	103: "liquid temperature",
	104: "dissolved oxygen",
	105: "liquid level", 
	106: "liquid level",
	107: "liquid level",
	108: "liquid level",
	109: "liquid level",
	110: "flow meter",
	111: "flow meter",
	112: "liquid level",

	201: "soil temperature", 
	202: "soil temperature",
	203: "soil temperature",
	205: "electrical conductivity",
	206: "pH",
	208: "moisture",
	209: "moisture",
	210: "moisture",
	211: "moisture",

	301: "relative humidity and air temperature",
	302: "relative humidity and air temperature",
	303: "total pressure",
	304: "oxygen",
	305: "carbon dioxide",
	306: "photosynthetically active radiation",

	401: "relative humidity and air temperature",
	402: "total pressure",
	403: "photosynthetically active radiation"}
```

#### Methods

It should be noted beforehand that the RHTemp sensors return two values.

```python
test_sensor.read()
test_RHTemp.read()
```

This returns a (two) random value(s) that will cross both HSST's.

```python
test_sensor.read_low()
test_RHTemp.read_low()
```

This returns a (two) value(s) guaranteed to be below the HSST value.

```python
test_sensor.read_high()
test_RHTemp.read_high()
```

This returns a (two) value(s) guaranteed to be above the HSST value.

### Test actuators

In order to import the test actuators type:

```python
from API.test_actuators import F, V, M, P
```

This gives you access to the following dictionaries:

```python
# filters
F = {1: test_actuator("UV filter")}

# solenoid valves
V = {3: test_actuator("CO2 solenoid"),
     4: test_actuator("N2 solenoid")}

# no idea what M stands for
M = {1:  test_actuator("heater"),
     2:  test_actuator("chiller"),
     6:  test_actuator("fan 1"),
     7:  test_actuator("fan 2"),
     8:  test_actuator("O2 concentrator"),
     18: test_actuator("LED")}

# pumps
P = {1:  test_actuator("main pump"),
     2:  test_actuator("condensate pump"),
     3:  test_actuator("nutrient 1 dosing"),
     4:  test_actuator("nutrient 2 dosing"),
     5:  test_actuator("pH dosing"),
     6:  test_actuator("nutrient 1 circulation"),
     7:  test_actuator("air bubbler"),
     8:  test_actuator("filter pump"),
     9:  test_actuator("nutrient 2 circulation"),
     10: test_actuator("humidifier pump"),
     11: test_actuator("main tank circulation"),
     12: test_actuator("dehumidifier")}
```

#### Methods

```python 
test_actuator.check_status()
```

Returns either the string "on" or "off".

```python 
test_actuator.toggle()
```

Switches the status of the actuator.

If further clarification is required, the business school is just south of the Engineering Center.
