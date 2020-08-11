from django import forms 
from mylist_app.models import Tasklist
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    class Meta:
        model=Tasklist
        fields = ['task','done']
