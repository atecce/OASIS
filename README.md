# OASIS

This is just to get started, most of the code is to get familiar with the problem, and I am in no sense attached to it. That being said, while I don't think the main function will survive very long, I'm sure the sensors and components should be handled as objects in some form. We could abstract away from them interfacing with the hardware by defining the classes well, and then build the algorithms we need with the objects, never having to actually worry about how they interact. That could be a line we split the labor up with.

The references folder has the initial submission documents and one of the references at the bottom of it. I want to see if I can track down all of them and get them in there. It also has a glance of some of the algorithms they had in mind. It didn't seem like they were particulary attached to the ones they have, so maybe we can come up with something better, but there diagram should probably be the first iteration as we get ourselves acquainted with the problem.

Adafruit is a library for interacting with Beaglebone, which I am certain we will need at some point to interact with the hardware with its IO module.  It's README has installation instructions (just enter the directory and it's in the same format you're staring at right now). I have mine installed on a VM in Ubuntu because OS X isn't supported (perhaps I should use the same distribution as Beaglebone's). Let me know if any of you have a better one in mind. Henrik, you said you had experience with this hardware right? Catch us all up to speed.

So I think a good approach right now is to think of this in two parts. Building an API to interact with the hardware and building the algorithms out of the API. Let me know what you guys think.
