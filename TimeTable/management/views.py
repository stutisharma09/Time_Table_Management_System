from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Welcome to the Time Table Management Website!</h1>")


# Create your views here.
