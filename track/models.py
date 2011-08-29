from django.db import models
from django.contrib.auth.models import User, Group
import datetime


MEASUREMENT_CHOICES = (
	(u'WAST', u'Waist'),
	(u'WGHT', u'Weight'),
	(u'BPSY', u'Systolic Blood Presure'),
)

class Event(models.Model):
    EVENT_TYPES = (
	(u'RUN',  u'Run'),
	(u'SWIM', u'Swim'),
	(u'WALK', u'Walk'),
	(u'YOGA', u'Yoga'),
	(u'CHES', u'Chess'),
	(u'EAT',  u'Eat'),
	(u'DRNK', u'Drink'),
    )
    type = models.CharField(max_length=4, choices=EVENT_TYPES, verbose_name="type")
    start = models.DateTimeField('Start')
    end = models.DateTimeField('End')
    def __unicode__(self):
        return self.type

class Measurement(models.Model):
    type = models.CharField(max_length=4, choices=MEASUREMENT_CHOICES, verbose_name="type")
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Value")
    unit = models.CharField(max_length=16)
    timestamp = models.DateField(verbose_name="When")
    class Meta:
	verbose_name_plural = "Measurements"
	verbose_name = "Measurement"
    def __unicode__(self):
        return self.type

class PhysicalActivity(models.Model):
    event = models.OneToOneField(Event, verbose_name="Event")
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    reps = models.PositiveIntegerField(verbose_name="Repetitions")
    caloriesBurnt = models.PositiveIntegerField(verbose_name="Calories Burnt")
    owner = models.ForeignKey(User, verbose_name="owner")
    class Meta:
	verbose_name_plural = "Physical Activities"
	verbose_name = "Physical Activity"
    def __unicode__(self):
        return self.event.type

class DietActivity(models.Model):
    MEAL_TYPES = (
	(u'BRKF', u'Breakfast'),
	(u'LNCH', u'Lunch'),
	(u'DINR', u'Dinner'),
	(u'OTHR', u'Other'),
    )
    event = models.OneToOneField(Event, verbose_name="Event")
    mealType = models.CharField(max_length=4, choices=MEAL_TYPES, verbose_name="Meal Types")
    owner = models.ForeignKey(User, verbose_name="owner")
    class Meta:
	verbose_name_plural = "Diet Activities"
	verbose_name = "Diet Activity"
    def __unicode__(self):
        return self.event.type

class HobbyActivity(models.Model):
    event = models.OneToOneField(Event, verbose_name="Event")
    owner = models.ForeignKey(User, verbose_name="owner")
    class Meta:
	verbose_name_plural = "Hobby Activities"
	verbose_name = "Hobby Activity"
    def __unicode__(self):
        return self.event.type

class TargetMeasurement(models.Model):
    type = models.CharField(max_length=4, choices=MEASUREMENT_CHOICES, verbose_name="type")
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Target")
    unit = models.CharField(max_length=16)
    class Meta:
	verbose_name_plural = "Target Measurements"
	verbose_name = "Target Measurement"
    def __unicode__(self):
        return self.type

class MyStats(models.Model):
    weightTarget = models.OneToOneField(TargetMeasurement, null=True, blank=True, related_name='weight', verbose_name="Target Weight")
    waistTarget = models.OneToOneField(TargetMeasurement, null=True, blank=True, related_name='waist', verbose_name="Target Waist")
    sysBloodPressureTarget = models.OneToOneField(TargetMeasurement, null=True, blank=True, related_name='bp', verbose_name="Target Systolic Blood Pressure")
    owner = models.OneToOneField(User, verbose_name="owner")
    class Meta:
	verbose_name_plural = "MyStats"
	verbose_name = "MyStats"
    def __unicode__(self):
        return self.owner.username

