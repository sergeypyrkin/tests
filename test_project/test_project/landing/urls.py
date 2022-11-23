from django.http import HttpResponse


from django.urls import path, include
from . import views

urlpatterns = [

    path('landing/', views.landing, name='landing')
]