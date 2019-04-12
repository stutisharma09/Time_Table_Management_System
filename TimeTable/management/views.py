from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the Time TimeTable Management Website!")
# Create your views here.
