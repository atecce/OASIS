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
