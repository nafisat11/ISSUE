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

<<<<<<< HEAD
class Buildings(models.Model):
    name = models.CharField(max_length = 200)

    def get_building_name(self):
        return self.name
    def get_building_id(self):
        return self.id

class Floors(models.Model):
    building = models.ForeignKey(Buildings, on_delete=models.PROTECT)
    number = models.IntegerField() 
    
    def get_building_id(self):
        return self.building
    def get_floor_number(self):
        return self.number
    def get_floor_id(self):
        return self.id

class Rooms(models.Model):
    floor = models.ForeignKey(Floors, on_delete=models.PROTECT)
    room_number = models.IntegerField()
    max_occupancy = models.IntegerField()
    max_pandemic_occupancy = models.IntegerField()
    blueprint = models.URLField()

    def get_floor_id(self):
        return self.floor
    def get_room_number(self):
        return self.room_number
    def get_room_id(self):
        return self.id
    def get_max_occupancy(self):
        return self.max_occupancy
    def get_max_pandemic_occupancy(self):
        return self.max_pandemic_occupancy
    def get_blueprint(self):
        return self.blueprint

class Heatmaps(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    probabilities = ArrayField(
        ArrayField(models.DecimalField(max_digits=11, decimal_places=10))
    )
    
    def get_user(self):
        return self.user
    def get_probabilities(self):
        return self.probabilities
=======

class Users(models.Model):
    pass  # By default, Django adds an id field


class Buildings(models.Model):
    name = models.CharField(max_length=200)


class Floors(models.Model):
    building_id = models.ForeignKey(Buildings, on_delete=models.PROTECT)
    number = models.IntegerField()


class Rooms(models.Model):
    floor_id = models.ForeignKey(Floors, on_delete=models.PROTECT)
    room_number = models.IntegerField()
    max_occupancy = models.IntegerField()
    blueprint = models.URLField()


class Heatmaps(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    probabilities = ArrayField(
        ArrayField(models.DecimalField(max_digits=11, decimal_places=10))
    )
>>>>>>> creates db schema
