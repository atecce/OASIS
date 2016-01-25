#include <stdio.h>

class sensor {

	public:

		sensor(char *, int);
		float read();

};

sensor::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

	// This method depends on quite a bit. Depending on the data communication
	// type and the sensor, it will use different libraries and return different 
	// values.
	//def read(self): pass 

class EC : public sensor {

	char *units		  = " micro-S-cm-l";
	char *data_comm	    	  = "I2C";
	float sensor_range[2]     = {3, 3000};
	float required_resolution = 1;
};

EC::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

class pH : public sensor {

	char *units		  = "pH";
	char *data_comm	          = "I2C";
	float sensor_range[2]     = {2, 12};
	float required_resolution = .2;
};

pH::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

class temperature : public sensor {

	char *units		  = "C";
	char *data_comm	          = "one-wire";
	float sensor_range[2]     = {0, 100};
	float required_resolution = 1;
};

temperature::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

class moisture : public sensor {

	char *units		  = "%";
	char *data_comm	          = "ADC-I2C";
	float sensor_range[2]     = {0, 50};
	float required_resolution = 1;
};

moisture::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

class DO_probe : public sensor {

	char *units		  = "mg/L";
	char *data_comm	          = "I2C";
	float sensor_range[2]     = {0, 15};
	float required_resolution = .1;
};

DO_probe::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

class liquid_level : public sensor {

	char *units		  = "cm";
	char *data_comm	          = "ADC-I2C";
	float sensor_range[2]     = {0, 40.5};
	float required_resolution = 1.25;
};

liquid_level::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

class flow_meter : public sensor {

	char *units		  = "gpm";
	char *data_comm	          = "UART";
	float sensor_range[2]     = {.2, 2};
	float required_resolution = .05;
};

flow_meter::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

class RH_temp : public sensor {

	char *units		  = "(C, %)";
	char *data_comm	          = "one-wire";
	float sensor_range[2]     = {5, 99};
	float required_resolution = 1;
};

RH_temp::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

class total_pressure : public sensor {

	char *units		  = "kPA";
	char *data_comm	          = "I2C";
	float sensor_range[2]     = {30, 110};
	float required_resolution = 1;
};

total_pressure::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

class oxygen : public sensor {

	char *units		  = "%";
	char *data_comm	          = "ADC-I2C";
	float sensor_range[2]     = {0, 100};
	float required_resolution = 1;
};

oxygen::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

class CO2 : public sensor {

	char *units		  = "ppm";
	char *data_comm	          = "UART";
	float sensor_range[2]     = {0, 2000};
	float required_resolution = 100;
};

CO2::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

class light_PAR : public sensor {

	char *units		  = "micro-mol per meters-squared seconds";
	char *data_comm	          = "ADC-I2C";
	float sensor_range[2]     = {0, 2000};
	float required_resolution = 2;
};

light_PAR::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

class camera : public sensor {

	char *units		  = "RGB";
	char *data_comm	          = "USB";
	float sensor_range[2]     = {1, 255};
	float required_resolution = "1k0x1k";
};

camera::sensor(char *name, int pin) {

	// these are determined at construction
	name = name;
	pin  = pin;
}

// liquid tanks and plumbing
S101 =           EC("S101", 0x66);
S102 =           pH("S102", 0x65);
S103 =  temperature("S103", NULL);
S104 =     DO_probe("S104", 0x61);
S105 = liquid_level("S105", NULL);
S106 = liquid_level("S106", NULL);
S107 = liquid_level("S107", NULL);
S108 = liquid_level("S108", NULL);
S109 = liquid_level("S109", NULL);
S110 =   flow_meter("S110", NULL);
S111 =   flow_meter("S111", NULL);
S112 = liquid_level("S112", NULL);

// growth medium
S201 = temperature("S201", NULL);
S202 = temperature("S202", NULL);
S203 = temperature("S203", NULL);
S204 = temperature("S204", NULL);
S205 =          EC("S205", NULL);
S206 =          pH("S206", NULL);
S208 =    moisture("S208", NULL);
S209 =    moisture("S209", NULL);
S210 =    moisture("S210", NULL);
S211 =    moisture("S211", NULL);

// internal atmosphere
S301 =        RH_temp("S301", NULL);
S302 =        RH_temp("S302", "P8_9");
S303 = total_pressure("S303", 0x77);
S304 =         oxygen("S304", NULL);
S305 =            CO2("S305", NULL);
S306 =      light_PAR("S306", NULL);
S307 =         camera("S307", NULL);

// external environment
S401 =        RH_temp("S401", "P8_10");
S402 = total_pressure("S402", NULL);
S403 =      light_PAR("S403", NULL);

sensor sensor_suite[32] = {S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, 
	                   S201, S202, S203, S204, S205, S206,       S208, S209, S210, S211,
	                   S301, S302, S303, S304, S305, S306, S307,
	                   S401, S402, S403};
