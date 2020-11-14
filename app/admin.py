# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Buildings, Floors, Rooms, Heatmaps

# Register your models here.
admin.site.register(Buildings)
admin.site.register(Floors)
admin.site.register(Rooms)
admin.site.register(Heatmaps)