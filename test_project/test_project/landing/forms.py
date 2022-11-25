from django.forms import ModelForm
from .models import *


# Create the form class.
class SubsriberForm(ModelForm):
    class Meta:
        model = Subscriber
        exclude = ['']
