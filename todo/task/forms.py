from django import forms
from django.forms import ModelForm

from .models import *

class taskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'