#include <stdio.h>
#include "actuators.h"

int main()
{
	actuator F1 = actuator("S101", "0x66");
	actuator F2 = actuator("S102", "0x65");
	actuator F3 = actuator("S103", NULL);
	actuator F4 = actuator("S104", "0x61");
	actuator F5 = actuator("S105", NULL);

	actuator M01 = actuator("S106", NULL);
	actuator M02 = actuator("S106", NULL);
	actuator M03 = actuator("S106", NULL);

	actuator M05 = actuator("S106", NULL);
	actuator M07 = actuator("S107", NULL);
	actuator M08 = actuator("S108", NULL);
	actuator M09 = actuator("S109", NULL);
	actuator M10 = actuator("S110", NULL);
	actuator M11 = actuator("S111", NULL);
	actuator M12 = actuator("S112", NULL);
	
	actuator M15 = actuator("S112", NULL);
	actuator M16 = actuator("S112", NULL);
	actuator M17 = actuator("S112", NULL);
	actuator M18 = actuator("S112", NULL);
	actuator M19 = actuator("S112", NULL);

	actuator P01 = actuator("S201", NULL);
	actuator P02 = actuator("S202", NULL);
	actuator P03 = actuator("S203", NULL);
	actuator P04 = actuator("S204", NULL);
	actuator P05 = actuator("S205", NULL);
	actuator P06 = actuator("S206", NULL);
	actuator P07 = actuator("S206", NULL);
	actuator P08 = actuator("S208", NULL);
	actuator P09 = actuator("S209", NULL);
	actuator P10 = actuator("S210", NULL);
	actuator P11 = actuator("S211", NULL);
	actuator P12 = actuator("S211", NULL);

	actuator R01 = actuator("S301", NULL);
	actuator R02 = actuator("S302", "P8_9");

	actuator T03 = actuator("S303", "0x77");
	actuator T03 = actuator("S303", "0x77");
	actuator T03 = actuator("S303", "0x77");
	actuator T04 = actuator("S304", NULL);
	actuator T05 = actuator("S305", NULL);
	actuator T06 = actuator("S306", NULL);
	actuator T07 = actuator("S307", NULL);
	actuator T08 = actuator("S307", NULL);
	actuator T09 = actuator("S307", NULL);

	actuator V402 = actuator("S402", NULL);
	actuator V403 = actuator("S403", NULL);
	actuator V404 = actuator("S403", NULL);
	actuator V405 = actuator("S403", NULL);

	actuator V407 = actuator("S403", NULL);

	actuator Z01 = actuator("S201", NULL);
	actuator Z02 = actuator("S202", NULL);
	actuator Z03 = actuator("S203", NULL);
	actuator Z04 = actuator("S204", NULL);
	actuator Z05 = actuator("S205", NULL);
	actuator Z06 = actuator("S206", NULL);
	actuator Z07 = actuator("S206", NULL);
	actuator Z08 = actuator("S208", NULL);
	actuator Z09 = actuator("S209", NULL);
	actuator Z10 = actuator("S210", NULL);
	actuator Z11 = actuator("S211", NULL);
	actuator Z12 = actuator("S211", NULL);
	actuator Z13 = actuator("S211", NULL);
}
