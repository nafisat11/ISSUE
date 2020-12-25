# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import Buildings, Floors, Rooms, Heatmaps
from .agent_based_infection_probability import AttackRates

import json


@login_required(login_url="/login/")
def index(request):

    context = {}
    context['segment'] = 'index'
    context['buildings'] = Buildings.objects.all()

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


def get_floors(request):
    if request.method == "GET" and request.is_ajax():
        # get name of user selected building
        building_name = request.GET.get("building", None)

        result_set = []
        all_floors = []

        selected_building = Buildings.objects.get(
            name=str(building_name))  # get field object that matches the selected building

        # return instances of floors that match the building, backward relationship
        all_floors = selected_building.floors_set.all()
        for floor in all_floors:
            result_set.append(
                {'floor_id': floor.id, 'floor_number': floor.number})  # floor_id that corresponds to each floor option

        return HttpResponse(json.dumps(result_set), content_type="application/json")

    else:
        return redirect('/')


def get_rooms(request):
    if request.method == "GET" and request.is_ajax():
        floor_id = request.GET.get("floor_id", None)  # retrieve all floor_ids

        result_set = []
        # filter the rooms that match the floor_id in rooms table
        selected_floor = Rooms.objects.filter(floor_id=floor_id)

        for rooms in selected_floor:
            result_set.append({'room_number': rooms.room_number})

        return HttpResponse(json.dumps(result_set), content_type="application/json")

    else:
        return redirect('/')


def get_attack_rates(request):
    if request.method == "GET" and request.is_ajax():
        # TODO: retrieve the seat selections from the ajax request, hardcoded for now
        # seat_selections = request.GET.get("seat_selections", None)
        agents = [
            {
                'id': 1,
                'x': 0.0,
                'y': 0.0,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 2,
                'x': 0.5,
                'y': 0.0,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 3,
                'x': 1.0,
                'y': 0.0,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 4,
                'x': 1.5,
                'y': 0.0,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 5,
                'x': 2.0,
                'y': 0.0,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 6,
                'x': 0.0,
                'y': 0.4,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 7,
                'x': 0.5,
                'y': 0.4,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 8,
                'x': 1.0,
                'y': 0.4,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 9,
                'x': 1.5,
                'y': 0.4,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 10,
                'x': 2.0,
                'y': 0.4,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 11,
                'x': 0.0,
                'y': 0.8,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 12,
                'x': 0.5,
                'y': 0.8,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 13,
                'x': 1.0,
                'y': 0.8,
                'z': None,
                'state': 2,
                'attRate': 0.05
            },
            {
                'id': 14,
                'x': 1.5,
                'y': 0.8,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 15,
                'x': 2.0,
                'y': 0.8,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 16,
                'x': 0.0,
                'y': 1.2,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 17,
                'x': 0.5,
                'y': 1.2,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 18,
                'x': 1.0,
                'y': 1.2,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 19,
                'x': 1.5,
                'y': 1.2,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 20,
                'x': 2.0,
                'y': 1.2,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 21,
                'x': 0.0,
                'y': 1.6,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 22,
                'x': 0.5,
                'y': 1.6,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 23,
                'x': 1.0,
                'y': 1.6,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 24,
                'x': 1.5,
                'y': 1.6,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
            {
                'id': 25,
                'x': 2.0,
                'y': 1.6,
                'z': None,
                'state': 1,
                'attRate': 0.05
            },
        ]
        attack_rates = AttackRates(agents).probabilities()
        return HttpResponse(json.dumps({'attack_rates': attack_rates}), content_type="application/json")


def selection_submitted(request):
    if request.method == "GET" and request.is_ajax():
        room_number = request.GET.get("room", None)
        floor_id = request.GET.get("floor_id", None)

        selected_room = Rooms.objects.get(
            room_number=room_number, floor_id=floor_id)

        return HttpResponse(json.dumps({'max_occupancy': selected_room.max_occupancy,
                                        'max_pandemic_occupancy': selected_room.max_pandemic_occupancy}),
                            content_type="application/json")

    else:
        return redirect('/')
