# OASIS

I think a good approach right now is to think of this in two parts. Building an API to interact with the hardware and building the algorithms out of the API. Let me know what you guys think. The objects and functions folder roughly delineate these two pieces. This is just to get started, most of the code is to get familiar with the problem, and I am in no sense attached to it. 

Adafruit is a library for interacting with Beaglebone, which I am certain we will need at some point to interact with the hardware with its IO module.  It's README has installation instructions (just enter the directory and it's in the same format you're staring at right now). I have mine installed on a VM in Ubuntu because OS X isn't supported (perhaps I should use the same distribution as Beaglebone's). Let me know if any of you have a better one in mind. Henrik, you said you had experience with this hardware right? Catch us all up to speed.

We are going to need to use threading extensively, as different components run in parallel, just a heads up.
