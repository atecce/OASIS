unsigned int time = 0;

typedef enum state {germinate, autopilot, standby, shutdown}

unsigned const int memories = 0;

float observations[memories];

state mode = standby;

int main() {

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
