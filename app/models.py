# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Users(models.Model):
    pass

class Buildings(models.Model):
    name = models.CharField(max_length = 200)

class Floors(models.Model):
    building = models.ForeignKey(Buildings, on_delete=models.PROTECT)
    number = models.IntegerField() 

class Rooms(models.Model):
    floor = models.ForeignKey(Floors, on_delete=models.PROTECT)
    room_number = models.IntegerField()
    max_occupancy = models.IntegerField()
    blueprint = models.URLField()

class Heatmaps(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    probabilities = ArrayField(
        ArrayField(models.DecimalField(max_digits=11, decimal_places=10))
    )