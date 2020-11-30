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
    name = models.CharField(max_length=200)

    def get_building_name(self):
        return self.name

    def get_building_id(self):
        return self.id

    def __str__(self):
        return self.name


class Floors(models.Model):
    building = models.ForeignKey(Buildings, on_delete=models.PROTECT)
    # might have to change this to char if we want to include B1, B2 basement floors
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
    room = models.ForeignKey(Rooms, on_delete=models.PROTECT)

    def get_user(self):
        return self.user

    def get_probabilities(self):
        return self.probabilities

    def get_room(self):
        return self.room
