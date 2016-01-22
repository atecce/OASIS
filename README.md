# OASIS

If anyone wants to start on the web development stuff, there's a lot to be done there. Setting up a database, making the GUI on the website nicer, etc. We will ultimately need to integrate the sensor collection into this part (right now I'm thinking that the sensor data just gets sent to a server immediately and only the current sensor data is used to act). They should have some of this in the cloud9 directory, although I don't think much of that is ultimately wise to use.
  		  
 -Adafruit is a library for interacting with Beaglebone, which I am certain we will need at some point to interact with the hardware using the IO module.  It's README has installation instructions (just enter the directory and it's in the same format you're staring at right now). 		 +For the control logic itself, I would like to finish the API first so as not to specify methods that I later find out can't be implemented.
  		  
 -We are going to need to use threading extensively, as different components run in parallel, just a heads up. Python has a thread library however, this may or may not be sufficient enough. 		 +Otherwise, I will try to keep on ongoing to-do list on what is needed to finish the API in that directory's README. I expect it to change quickly.

