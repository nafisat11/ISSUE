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

def get_probabilities(request):
    if request.method == "GET" and request.is_ajax():
        # get name of user selected building
        user_id = request.GET.get("user_id", None)
        room_id = request.GET.get("room_id", None)
        selected_heatmap = Heatmaps.objects.filter(
            user_id=user_id, room_id=room_id)  # get field object that matches the selected building

        return HttpResponse(json.dumps(selected_heatmap.probabilities), content_type="application/json")

    else:
        return redirect('/')
