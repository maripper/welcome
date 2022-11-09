from django.shortcuts import render

import requests as req

from django.http import JsonResponse,HttpResponse  

import random

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

import json

import ast

# perform business logic

@csrf_exempt

def welcome(request):

    return render(request,"home.html",{})

    # perform business logic

@csrf_exempt

def timeline(request):

    return render(request,"timeline.html",{})

@csrf_exempt

def doc(request):

    return render(request,"doc.html",{})

@csrf_exempt  

def start(request):

    n = request.POST
    return JsonResponse({'sender_and_receiver_comparing_sample_equivalent':'response'})
