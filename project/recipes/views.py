from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('a home do recipes')


def about(request):
    return HttpResponse('about')


def contact(requst):
    return HttpResponse('contact')
