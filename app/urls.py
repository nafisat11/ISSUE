# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('get_floors/', views.get_floors, name='get-floors'),
    path('get_rooms/', views.get_rooms, name='get-rooms'),
    path('selection_submitted/', views.selection_submitted,
         name='selection-submitted'),
    path('post_attack_rates/', views.post_attack_rates, name='post-attack-rates'),
    path('post_seat_selections/', views.post_seat_selections,
         name='post-seat-selections')

]
