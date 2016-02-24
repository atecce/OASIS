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
     101:  test_sensor("electrical_conductivity", 1150, 1250),
     102:  test_sensor("ph_and_circuitry",         5.5,    6),     
     103:  test_sensor("liquid_temp", 		    22,   24),
#     104:   I2C_sensor("do_probe_and_circuitry",   0x61),
#     105: liquid_level("liquid_level", 	    0x80), 
#     106: liquid_level("liquid_level", 	    0xA0),
#     107: liquid_level("liquid_level", 	    0xC0),
#     108: liquid_level("liquid_level", 	    0xE0),
#     109: liquid_level("liquid_level", 	    0xD0),
#     110:   flow_meter("flow_meter_and_circuitry", 1),
#     111:   flow_meter("flow_meter_and_circuitry", 4),
#     112: liquid_level("liquid_level", 	    0xF0),

     # growth medium
     201: test_sensor("soil_temp", 15, 20), 
     202: test_sensor("soil_temp", 15, 20),
     203: test_sensor("soil_temp", 15, 20),
     205: test_sensor("electrical_conductivity", 1150, 1250),
     206: test_sensor("ph_and_circuitry",         5.5,    6),
#     208:    moisture("moisture", 0x80),
#     209:    moisture("moisture", 0xA0),
#     210:    moisture("moisture", 0xC0),
#     211:    moisture("moisture", 0xE0),

     # internal atmosphere
     301: test_RHTemp(),
     302: test_RHTemp(),
     303: test_sensor("total_pressure", 80, 84),
#     304:      oxygen("O2"),
     305: test_sensor("CO2",   1000, 2000),
     306: test_sensor("light",  200,  250),

     # external environment
     401: test_RHTemp(),
     402: test_sensor("total_pressure", 80,  84),
     403: test_sensor("light",         200, 250)}
```

The parameters just determine the name and HSST values (notice the commented out sensors, I did not have immediate access to those HSST's. We have a nice feedback loop here, so let me know when you find those.)

They are denoted by their SysID, this is advantageous because they are categorized by the environment in which they are in (which is described in the comments.) However, I might later add an alternative notation which just indexes by sensor type (which is what Noah primarily uses).

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
# need this for test actuator class
from test_API import test_actuator

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
