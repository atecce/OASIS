# OASIS

I think a good approach right now is to think of this in two parts. Building an API to interact with the components and building the algorithms out of the API. Let me know what you guys think. The objects and functions folder roughly delineate these two pieces. The code up now is just to get familiar with the problem, and I am in no sense attached to it. 

Adafruit is a library for interacting with Beaglebone, which I am certain we will need at some point to interact with the hardware using the IO module.  It's README has installation instructions (just enter the directory and it's in the same format you're staring at right now). 

We are going to need to use threading extensively, as different components run in parallel, just a heads up.
