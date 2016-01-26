#include <stdio.h>

class sensor {

	public:

		sensor(const char *name, const char *pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}

		float read();
};

	// This method depends on quite a bit. Depending on the data communication
	// type and the sensor, it will use different libraries and return different 
	// values.
	//def read(self): pass 

//class EC : public sensor {
//
//	char *units		  = " micro-S-cm-l";
//	char *data_comm	    	  = "I2C";
//	float sensor_range[2]     = {3, 3000};
//	float required_resolution = 1;
//
//	public:
//
//		EC(char *name, int pin) : sensor(char *name, int pin)
//};
//
//class pH : public sensor {
//
//	char *units		  = "pH";
//	char *data_comm	          = "I2C";
//	float sensor_range[2]     = {2, 12};
//	float required_resolution = .2;
//
//	public:
//
//		pH(char *name, int pin) : sensor(char *name, int pin)
//};
//
//class temperature : public sensor {
//
//	char *units		  = "C";
//	char *data_comm	          = "one-wire";
//	float sensor_range[2]     = {0, 100};
//	float required_resolution = 1;
//
//	public:
//
//		temperature(char *name, int pin) : sensor(char *name, int pin)
//};
//
//class moisture : public sensor {
//
//	char *units		  = "%";
//	char *data_comm	          = "ADC-I2C";
//	float sensor_range[2]     = {0, 50};
//	float required_resolution = 1;
//
//	public:
//
//		moisture(char *name, int pin) : sensor(char *name, int pin)
//};
//
//class DO_probe : public sensor {
//
//	char *units		  = "mg/L";
//	char *data_comm	          = "I2C";
//	float sensor_range[2]     = {0, 15};
//	float required_resolution = .1;
//
//	public:
//
//		DO_probe(char *name, int pin) : sensor(char *name, int pin)
//};
//
//class liquid_level : public sensor {
//
//	char *units		  = "cm";
//	char *data_comm	          = "ADC-I2C";
//	float sensor_range[2]     = {0, 40.5};
//	float required_resolution = 1.25;
//
//	public:
//
//		liquid_level(char *name, int pin) : sensor(char *name, int pin)
//};
//
//class flow_meter : public sensor {
//
//	char *units		  = "gpm";
//	char *data_comm	          = "UART";
//	float sensor_range[2]     = {.2, 2};
//	float required_resolution = .05;
//
//	public:
//
//		flow_meter(char *name, int pin) : sensor(char *name, int pin)
//};
//
//class RH_temp : public sensor {
//
//	char *units		  = "(C, %)";
//	char *data_comm	          = "one-wire";
//	float sensor_range[2]     = {5, 99};
//	float required_resolution = 1;
//
//	public:
//
//		RH_temp(char *name, int pin) : sensor(char *name, int pin)
//};
//
//class total_pressure : public sensor {
//
//	char *units		  = "kPA";
//	char *data_comm	          = "I2C";
//	float sensor_range[2]     = {30, 110};
//	float required_resolution = 1;
//
//	public:
//
//		total_pressure(char *name, int pin) : sensor(char *name, int pin)
//};
//
//class oxygen : public sensor {
//
//	char *units		  = "%";
//	char *data_comm	          = "ADC-I2C";
//	float sensor_range[2]     = {0, 100};
//	float required_resolution = 1;
//
//	public:
//
//		oxygen(char *name, int pin) : sensor(char *name, int pin)
//};
//
//class CO2 : public sensor {
//
//	char *units		  = "ppm";
//	char *data_comm	          = "UART";
//	float sensor_range[2]     = {0, 2000};
//	float required_resolution = 100;
//
//	public:
//
//		CO2(char *name, int pin) : sensor(char *name, int pin)
//};
//
//class light_PAR : public sensor {
//
//	char *units		  = "micro-mol per meters-squared seconds";
//	char *data_comm	          = "ADC-I2C";
//	float sensor_range[2]     = {0, 2000};
//	float required_resolution = 2;
//
//	public:
//
//		light_PAR(char *name, int pin) : sensor(char *name, int pin)
//};
//
//class camera : public sensor {
//
//	char *units		  = "RGB";
//	char *data_comm	          = "USB";
//	float sensor_range[2]     = {1, 255};
//	//float required_resolution = "1k0x1k";
//
//	public:
//
//		camera(char *name, int pin) : sensor(char *name, int pin)
//};

int main()
{
	//// liquid tanks and plumbing
	//sensor S101 =           EC("S101", 0x66);
	//sensor S102 =           pH("S102", 0x65);
	//sensor S103 =  temperature("S103", NULL);
	//sensor S104 =     DO_probe("S104", 0x61);
	//sensor S105 = liquid_level("S105", NULL);
	//sensor S106 = liquid_level("S106", NULL);
	//sensor S107 = liquid_level("S107", NULL);
	//sensor S108 = liquid_level("S108", NULL);
	//sensor S109 = liquid_level("S109", NULL);
	//sensor S110 =   flow_meter("S110", NULL);
	//sensor S111 =   flow_meter("S111", NULL);
	//sensor S112 = liquid_level("S112", NULL);
	//
	//// growth medium
	//sensor S201 = temperature("S201", NULL);
	//sensor S202 = temperature("S202", NULL);
	//sensor S203 = temperature("S203", NULL);
	//sensor S204 = temperature("S204", NULL);
	//sensor S205 =          EC("S205", NULL);
	//sensor S206 =          pH("S206", NULL);
	//sensor S208 =    moisture("S208", NULL);
	//sensor S209 =    moisture("S209", NULL);
	//sensor S210 =    moisture("S210", NULL);
	//sensor S211 =    moisture("S211", NULL);
	//
	//// internal atmosphere
	//sensor S301 =        RH_temp("S301", NULL);
	//sensor S302 =        RH_temp("S302", "P8_9");
	//sensor S303 = total_pressure("S303", 0x77);
	//sensor S304 =         oxygen("S304", NULL);
	//sensor S305 =            CO2("S305", NULL);
	//sensor S306 =      light_PAR("S306", NULL);
	//sensor S307 =         camera("S307", NULL);
	//
	//// external environment
	//sensor S401 =        RH_temp("S401", "P8_10");
	//sensor S402 = total_pressure("S402", NULL);
	//sensor S403 =      light_PAR("S403", NULL);
	//
	// liquid tanks and plumbing
	sensor S101 = sensor("S101", "0x66");
	sensor S102 = sensor("S102", "0x65");
	sensor S103 = sensor("S103", NULL);
	sensor S104 = sensor("S104", "0x61");
	sensor S105 = sensor("S105", NULL);
	sensor S106 = sensor("S106", NULL);
	sensor S107 = sensor("S107", NULL);
	sensor S108 = sensor("S108", NULL);
	sensor S109 = sensor("S109", NULL);
	sensor S110 = sensor("S110", NULL);
	sensor S111 = sensor("S111", NULL);
	sensor S112 = sensor("S112", NULL);

	// growth medium
	sensor S201 = sensor("S201", NULL);
	sensor S202 = sensor("S202", NULL);
	sensor S203 = sensor("S203", NULL);
	sensor S204 = sensor("S204", NULL);
	sensor S205 = sensor("S205", NULL);
	sensor S206 = sensor("S206", NULL);
	sensor S208 = sensor("S208", NULL);
	sensor S209 = sensor("S209", NULL);
	sensor S210 = sensor("S210", NULL);
	sensor S211 = sensor("S211", NULL);

	// internal atmosphere
	sensor S301 = sensor("S301", NULL);
	sensor S302 = sensor("S302", "P8_9");
	sensor S303 = sensor("S303", "0x77");
	sensor S304 = sensor("S304", NULL);
	sensor S305 = sensor("S305", NULL);
	sensor S306 = sensor("S306", NULL);
	sensor S307 = sensor("S307", NULL);

	// external environment
	sensor S401 = sensor("S401", "P8_10");
	sensor S402 = sensor("S402", NULL);
	sensor S403 = sensor("S403", NULL);

	sensor sensor_suite[32] = {S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, 
				   S201, S202, S203, S204, S205, S206,       S208, S209, S210, S211,
				   S301, S302, S303, S304, S305, S306, S307,
				   S401, S402, S403};


	return 0;
}
