from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def landing(request):
    name = 'Sergey Pyrkin'
    return render(request, 'landing/landing.html', locals())

