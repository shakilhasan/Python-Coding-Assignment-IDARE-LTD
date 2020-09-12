from django import forms
from .models import Pipe
from django.contrib.auth.models import User


class PipeForm(forms.ModelForm):
    class Meta:
        model = Pipe
        #fields = ['user','name','phone','aphone','country','district','thana','address','total']
        fields = '__all__'
