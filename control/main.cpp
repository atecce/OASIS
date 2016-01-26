unsigned int time = 0;

typedef enum state {germinate, autopilot, standby}

unsigned const int memories = 0;

float observations[memories];

state mode = standby;

int main() {

	// signals from user, presumably
	while(some condition) {

		// dump all the sensor data to a server when capacity is reached
		if (memories == capacity) 
		{	
			forget();
			
			memories = 0;
		}

		switch(mode) {

			case germinate:

				germinate();

			case autopilot: 

				sense();
				act();

			// standby case
			default:

				prompt();
		}

		time++;
	}
	
	return 0;
}
