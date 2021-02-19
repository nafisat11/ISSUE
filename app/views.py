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
from .models import Buildings, Floors, Rooms
from django.views.decorators.csrf import csrf_protect, csrf_exempt

import json

agents = None


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
        agents = request.GET.get("seat_selections", None)
        duration = request.GET.get("duration", None)
        if agents is not None:
            attack_rates = AttackRates(
                agents, duration=duration).probabilities()
            # print(attack_rates)
            return HttpResponse(json.dumps({'attack_rates': attack_rates}), content_type="application/json")
        else:
            return redirect('/')


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


@csrf_exempt
def post_seat_selections(request):
    if request.method == "POST" and request.is_ajax():
        seat_selections = json.loads(request.POST.get('data'))
        # return HttpResponse(json.dumps({'seat_selections': seat_selections}), content_type="application/json")
        # print(seat_selections)
    # else:
        return redirect('/')
