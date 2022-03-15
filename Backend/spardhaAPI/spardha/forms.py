from django.forms import ModelForm
from .models import *

class UpdatePoints(ModelForm):
    class Meta:
        model = Score
        fields = ['hostel','points']
