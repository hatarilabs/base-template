# -*- encoding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

TIME_CHOICES = (
    ("Undefined", "Undefined"),
    ("Seconds", "Seconds"),
    ("Minutes", "Minutes"),
    ("Hours", "Hours"),
    ("Daysw", "Daysw"),
    ("Years", "Years"))

LENGTH_CHOICES = (
    ("Undefined", "Undefined"),
    ("Feet", "Feet"),
    ("Meters", "Meters"),
    ("Centimeters", "Centimeters"))

TIME_DICT = {
    "Undefined":0,
    "Seconds":1,
    "Minutes":2,
    "Hours":3,
    "Days":4,
    "Years":5 }

LENGTH_DICT = {
    "Undefined":0,
    "Feet":1,
    "Meters":2,
    "Centimeters":3 }

dateStr = '01-01-1970'
defaultDate = datetime.strptime(dateStr, '%m-%d-%Y').date()

def get_name(self):
    return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_name)

class Project(models.Model):
    modelName = models.CharField(max_length=50)
    modelDescription= models.TextField(default='')
    timeUnitName = models.CharField(max_length=50,default="Seconds",choices=TIME_CHOICES)
    lengthUnitName = models.CharField(max_length=50,default="Meters",choices=LENGTH_CHOICES)
    timeUnitCode = models.IntegerField(default=1)
    lengthUnitCode = models.IntegerField(default=2)
    epsgCode = models.IntegerField(default=32718)
    startDate = models.DateTimeField(default=defaultDate)
    created = models.DateTimeField(auto_now_add=True)
    token = models.SlugField(max_length=10,null=False, unique=True)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelName + '_' + self.token

    def get_token(self):
        return self.token

    def save(self,*args,**kwargs):
        if not self.token:
            self.token = get_random_string(10,'0123456789asdfghjklqwertyuiopzxcvbnmASDFGHJKLQWERTYUIOPZXCVBNM')
        self.timeUnitCode = 1 #TIME_DICT[self.timeUnitName]
        self.lengthUnitCode = 2 #LENGTH_DICT[self.lengthUnitName]
        super(Project,self).save(*args,**kwargs)

class SuscriptorType(models.Model):
    category = models.CharField(max_length=50)
    n_projects = models.IntegerField()
    ref_stages = models.IntegerField()
    n_cells = models.IntegerField()
    n_layers = models.IntegerField()
    n_periods = models.IntegerField()

    def __str__(self):
        return self.category


class SuscriptionRecords(models.Model):
    starting_date = models.DateTimeField()
    ending_date = models.DateTimeField()
    payment = models.FloatField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(SuscriptorType, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' license ' + self.category.category


@receiver(post_save, sender= User, dispatch_uid="update_subscription")
def update_subscription(sender, instance,created, **kwargs):
    if created:
        starting_date = datetime.now()
        ending_date =  starting_date + timedelta(days=3650)
        payment = 0
        user = instance
        category = SuscriptorType.objects.get(category="Freemium")
        update_suscription = SuscriptionRecords(starting_date=starting_date,ending_date = ending_date,payment = payment,user = user,category = category)
        update_suscription.save()
#https://stackoverflow.com/questions/13014411/django-post-save-signal-implementation
