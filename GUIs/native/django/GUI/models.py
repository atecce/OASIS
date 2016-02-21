from django.db import models

class User(models.Model): 

	email = models.EmailField()

class Sensor(models.Model):

	SysID    = models.IntegerField()
	function = models.CharField(max_length = 42)

class Actuator(models.Model): 

	SysID    = models.IntegerField()
	function = models.CharField(max_length = 42)

class Reading(models.Model): 

	sensor  = models.ForeignKey(Sensor)
	reading = models.FloatField(default = -1)

class Status(models.Model): 

	actuator = models.ForeignKey(Actuator)
	state    = models.NullBooleanField(default = None)
