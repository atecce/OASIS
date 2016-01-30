// need this to connect with database
#include "networking.h"

// start counter for time step
unsigned int time = 0;

// declare different possible states
typedef enum state {initiating, germinate, autopilot, standby, shutdown}

// initialize state
state mode = initiating;

float observation[sensor_amt]

// string for now, this is rather open-ended
char *choice;

void sense() {

	// thread this process for the duration of the program
	while(1) {
		
		// for each sensor, record the observation
		for (int i = 0; i < sensor_amt; i++) observation[i] = sensor_suite[i].read();

		// send observation to server
		dump(&observation);	
	}
}

void act() {

	// toggle each actuator
	for (int i = 0; i < actuator_amt; i++) actuator_suite[i].toggle();
}

void obey(char *choice) {

	// map the components to a list of natural numbers 0, 1, ..., sensor_amt + actuator_amt
	if      (choice == 0) 
	else if (choice == 1) 
		.
		.
		.
	else if (choice == sensor_amt + actuator_amt - 1)
}

int main() {

	// should start at system start up
	initiate();

	// sense as often as possible. the more data, the better, whether you're going to use it or not
	thread consciousness (sense);

	// signals from user, presumably
	while(mode != shutdown) {

		// decide what to do next based on what mode you are in
		switch(mode) {

			case germinate:

				germinate();

			case autopilot: 

				act();

			case standby:

				choice = prompt();
				obey(choice);

			case shutdown:

				break;

			default:

				userInputError();
		}

		time++;
	}

	system("shutdown -P now");

	return 0;
}
