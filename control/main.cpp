// start counter for time step
unsigned int time = 0;

// declare different possible states
typedef enum state {initiate, germinate, autopilot, standby, shutdown}

// initialize state
state mode = initiating;

int main() {

	// should start at system start up
	initiate();

	// signals from user, presumably
	while(mode != shutdown) {
        
        // sense as often as possible. the more data, the better, whether you're going to use it or not
		sense();

        // decide what to do next based on what mode you are in
		switch(mode) {

			case germinate:

				germinate();

			case autopilot: 

				act();
                
            case shutdown:
                
                system("shutdown -P now");

			// standby case
			default:

				choice = prompt();
                obey(choice);
		}

		time++;
	}
	
	return 0;
}
