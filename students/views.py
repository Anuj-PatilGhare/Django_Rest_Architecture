from django.shortcuts import render
from django.http import HttpResponse


def students(request):
    return HttpResponse("this is the page from Students App from core app")