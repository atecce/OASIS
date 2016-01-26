#include <stdio.h>

class sensor {

	public:

		sensor(const char *name, const char *pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}

		// This method depends on quite a bit. Depending on the data communication
		// type and the sensor, it will use different libraries and return different 
		// values.
		float read();
};

class EC : public sensor {

	const char *units	        = "micro-S-cm-l";
	const char *data_comm	        = "I2C";
	const float sensor_range[2]     = {3, 3000};
	const float required_resolution = 1;

	public:

		EC(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class pH : public sensor {

	const char *units	        = "pH";
	const char *data_comm	        = "I2C";
	const float sensor_range[2]     = {2, 12};
	const float required_resolution = .2;

	public:

		pH(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class temperature : public sensor {

	const char *units	        = "C";
	const char *data_comm	        = "one-wire";
	const float sensor_range[2]     = {0, 100};
	const float required_resolution = 1;

	public:

		temperature(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class moisture : public sensor {

	const char *units	        = "%";
	const char *data_comm	        = "ADC-I2C";
	const float sensor_range[2]     = {0, 50};
	const float required_resolution = 1;

	public:

		moisture(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class DO_probe : public sensor {

	const char *units	        = "mg/L";
	const char *data_comm	        = "I2C";
	const float sensor_range[2]     = {0, 15};
	const float required_resolution = .1;

	public:

		DO_probe(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class liquid_level : public sensor {

	const char *units	        = "cm";
	const char *data_comm	        = "ADC-I2C";
	const float sensor_range[2]     = {0, 40.5};
	const float required_resolution = 1.25;

	public:

		liquid_level(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class flow_meter : public sensor {

	const char *units	        = "gpm";
	const char *data_comm	        = "UART";
	const float sensor_range[2]     = {.2, 2};
	const float required_resolution = .05;

	public:

		flow_meter(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class RH_temp : public sensor {

	const char *units	        = "(C, %)";
	const char *data_comm	        = "one-wire";
	const float sensor_range[2]     = {5, 99};
	const float required_resolution = 1;

	public:

		RH_temp(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class total_pressure : public sensor {

	const char *units	        = "kPA";
	const char *data_comm	        = "I2C";
	const float sensor_range[2]     = {30, 110};
	const float required_resolution = 1;

	public:

		total_pressure(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class oxygen : public sensor {

	const char *units	        = "%";
	const char *data_comm	        = "ADC-I2C";
	const float sensor_range[2]     = {0, 100};
	const float required_resolution = 1;

	public:

		oxygen(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class CO2 : public sensor {

	const char *units	        = "ppm";
	const char *data_comm	        = "UART";
	const float sensor_range[2]     = {0, 2000};
	const float required_resolution = 100;

	public:

		CO2(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class light_PAR : public sensor {

	const char *units	        = "micro-mol per meters-squared seconds";
	const char *data_comm	        = "ADC-I2C";
	const float sensor_range[2]     = {0, 2000};
	const float required_resolution = 2;

	public:

		light_PAR(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class camera : public sensor {

	const char *units	    = "RGB";
	const char *data_comm	    = "USB";
	const float sensor_range[2] = {1, 255};
	//float required_resolution = "1k0x1k";

	public:

		camera(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

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
