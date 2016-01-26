#include <stdio.h>
#include "sensors.h"

int main()
{
	// liquid tanks and plumbing
	sensor S101 =           EC("S101", "0x66");
	sensor S102 =           pH("S102", "0x65");
	sensor S103 =  temperature("S103", NULL);
	sensor S104 =     DO_probe("S104", "0x61");
	sensor S105 = liquid_level("S105", NULL);
	sensor S106 = liquid_level("S106", NULL);
	sensor S107 = liquid_level("S107", NULL);
	sensor S108 = liquid_level("S108", NULL);
	sensor S109 = liquid_level("S109", NULL);
	sensor S110 =   flow_meter("S110", NULL);
	sensor S111 =   flow_meter("S111", NULL);
	sensor S112 = liquid_level("S112", NULL);
	
	// growth medium
	sensor S201 = temperature("S201", NULL);
	sensor S202 = temperature("S202", NULL);
	sensor S203 = temperature("S203", NULL);
	sensor S204 = temperature("S204", NULL);
	sensor S205 =          EC("S205", NULL);
	sensor S206 =          pH("S206", NULL);
	sensor S208 =    moisture("S208", NULL);
	sensor S209 =    moisture("S209", NULL);
	sensor S210 =    moisture("S210", NULL);
	sensor S211 =    moisture("S211", NULL);
	
	// internal atmosphere
	sensor S301 =        RH_temp("S301", NULL);
	sensor S302 =        RH_temp("S302", "P8_9");
	sensor S303 = total_pressure("S303", "0x77");
	sensor S304 =         oxygen("S304", NULL);
	sensor S305 =            CO2("S305", NULL);
	sensor S306 =      light_PAR("S306", NULL);
	sensor S307 =         camera("S307", NULL);
	
	// external environment
	sensor S401 =        RH_temp("S401", "P8_10");
	sensor S402 = total_pressure("S402", NULL);
	sensor S403 =      light_PAR("S403", NULL);
	
	sensor sensor_suite[32] = {S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, 
				   S201, S202, S203, S204, S205, S206,       S208, S209, S210, S211,
				   S301, S302, S303, S304, S305, S306, S307,
				   S401, S402, S403};
}
