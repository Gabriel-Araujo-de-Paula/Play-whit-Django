from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'gabby paula'
    })


def about(request):
    return HttpResponse('About')


def contact(requst):
    return HttpResponse('contact')
