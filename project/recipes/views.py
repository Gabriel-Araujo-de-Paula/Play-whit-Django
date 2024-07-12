from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'global/home.html')


def about(request):
    return HttpResponse('About')


def contact(requst):
    return HttpResponse('contact')
