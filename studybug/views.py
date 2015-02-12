#!/usr/bin/python

# Name: StudyBug 
# File: /StudyBugWeb/studybug/views.py
#
# Author(s): Grant McGovern
# Date: Tue 6 Jan 2015 
#
# URL: www.github.com/g12mcgov/StudyBug-Frontend
#
# ~ Django Views File ~
#
#

## Django Includes
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

# from mongoengine import *

## Third-Party Includes
import pymongo 
import datetime


def index(request):
    context = RequestContext(request)
    
    ## This is quite literally the most horrible idea ever...
    ## connecting AND querying to a database with each request... Temporary fix for 
    ## what has been the most annoying headache ever setting up MongoEngine to persist
    ## for the app's lifespan.
    
    username = ""
    password = ""

    # Establish a connection to Mongo 
    client = pymongo.MongoClient("mongodb://" + username + ":" + password + "@ds041581.mongolab.com:41581/heroku_app33177236")
    db = client.heroku_app33177236

    todayDate = datetime.datetime.now().strftime("%m/%d/%Y")
    
    # Retrieve rooms whose endate is the same as today's date 
    rooms = db.studybug.find_one({"endDate": todayDate})
    
    if rooms:
        if isinstance(rooms, list):
            # We first need to check if the rooms exist before we 'dict' it,
            # otherwise we'll get a "TypeError: 'NoneType' object is not iterable"
            rooms = dict(rooms)

            # In the pursuit of speed, use list comprehension
            timeRange = [room.encode('utf-8') for room in rooms['timeRange']]
            dataType = "list"

            # Extract our ROOM #
            roomNumber = rooms['room']
        else:
            timeRange = rooms['timeRange']      
            dataType = "string"
            roomNumber = rooms['room']
    else:
        timeRange = "No rooms available today"      
        dataType = "string"
        roomNumber = "N/A"


    return render_to_response('studybug/index.html', {'timeRange': timeRange, 'roomNumber': roomNumber, "dataType": dataType}, context)


