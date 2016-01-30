
// liquid tanks and plumbing
sensor S101 =           EC("S101", "0x66")
sensor S102 =           pH("S102", "0x65")
sensor S103 =  temperature("S103", NULL)
sensor S104 =     DO_probe("S104", "0x61")
sensor S105 = liquid_level("S105", NULL)
sensor S106 = liquid_level("S106", NULL)
sensor S107 = liquid_level("S107", NULL)
sensor S108 = liquid_level("S108", NULL)
sensor S109 = liquid_level("S109", NULL)
sensor S110 =   flow_meter("S110", NULL)
sensor S111 =   flow_meter("S111", NULL)
sensor S112 = liquid_level("S112", NULL)

// growth medium
sensor S201 = temperature("S201", NULL)
sensor S202 = temperature("S202", NULL)
sensor S203 = temperature("S203", NULL)
sensor S204 = temperature("S204", NULL)
sensor S205 =          EC("S205", NULL)
sensor S206 =          pH("S206", NULL)
sensor S208 =    moisture("S208", NULL)
sensor S209 =    moisture("S209", NULL)
sensor S210 =    moisture("S210", NULL)
sensor S211 =    moisture("S211", NULL)

// internal atmosphere
sensor S301 =        RH_temp("S301", NULL)
sensor S302 =        RH_temp("S302", "P8_9")
sensor S303 = total_pressure("S303", "0x77")
sensor S304 =         oxygen("S304", NULL)
sensor S305 =            CO2("S305", NULL)
sensor S306 =      light_PAR("S306", NULL)
sensor S307 =         camera("S307", NULL)

// external environment
sensor S401 =        RH_temp("S401", "P8_10")
sensor S402 = total_pressure("S402", NULL)
sensor S403 =      light_PAR("S403", NULL)

sensor_suite = (S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, 
		       S201, S202, S203, S204, S205, S206,       S208, S209, S210, S211,
		       S301, S302, S303, S304, S305, S306, S307,
		       S401, S402, S403)

F1 = actuator("F1")
F2 = actuator("F2")
F3 = actuator("F3")
F4 = actuator("F4")
F5 = actuator("F5")

M01 = actuator("M01")
M02 = actuator("M02")
M03 = actuator("M03")

M05 = actuator("M05")
M06 = actuator("M06")
M07 = actuator("M07")
M08 = actuator("M08")
M09 = actuator("M09")
M10 = actuator("M10")
M11 = actuator("M11")
M12 = actuator("M12")

M15 = actuator("M15")
M16 = actuator("M16")
M17 = actuator("M17")
M18 = actuator("M18")
M19 = actuator("M19")

P01 = actuator("P01")
P02 = actuator("P02")
P03 = actuator("P03")
P04 = actuator("P04")
P05 = actuator("P05")
P06 = actuator("P06")
P07 = actuator("P06")
P08 = actuator("P08")
P09 = actuator("P09")
P10 = actuator("P10")
P11 = actuator("P11")
P12 = actuator("P12")

R01 = actuator("R01")
R02 = actuator("R02")

T01 = actuator("T01")
T02 = actuator("T02")
T03 = actuator("T03")
T04 = actuator("T04")
T05 = actuator("T05")
T06 = actuator("T06")
T07 = actuator("T07")
T08 = actuator("T08")
T09 = actuator("T09")

V02 = actuator("V02")
V03 = actuator("V03")
V04 = actuator("V04")
V05 = actuator("V05")

V07 = actuator("V07")

Z01 = actuator("Z01")
Z02 = actuator("Z02")
Z03 = actuator("Z03")
Z04 = actuator("Z04")
Z05 = actuator("Z05")
Z06 = actuator("Z06")
Z07 = actuator("Z06")
Z08 = actuator("Z08")
Z09 = actuator("Z09")
Z10 = actuator("Z10")
Z11 = actuator("Z11")
Z12 = actuator("Z12")
Z13 = actuator("Z13")

actuator_suite = (F1,  F2,  F3,  F4,  F5,
		  M01, M02, M03,      M05, M06, M07, M08, M09, M10, M11, M12,           M15, M16, M17, M18, M19,
		  P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12,
		  R01, R02,
		  T01, T02, T03, T04, T05, T06, T07, T08, T09,
		       V02, V03, V04, V05,      V07, 
		  Z01, Z02, Z03, Z04, Z05, Z06, Z07, Z08, Z09, Z10, Z11, Z12, Z13)
