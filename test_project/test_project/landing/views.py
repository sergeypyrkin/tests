from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

# Create your views here.

def landing(request):
    name = 'Sergey Pyrkin'
    form = SubsriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])
        form.save()
    return render(request, 'landing/landing.html', locals())

