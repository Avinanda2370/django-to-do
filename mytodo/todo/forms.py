from django import forms
from django.forms import ModelForm
from .models import *



class TodoFrom(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Todo
        fields = '__all__'
