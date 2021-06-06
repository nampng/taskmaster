from django import forms
from django.forms.widgets import DateInput, TimeInput

class RoutineForm(forms.Form):
    text = forms.CharField(label='Routine', max_length=200)
    time = forms.TimeField(label='Time', widget=TimeInput(attrs={'type': 'time'}))

class TaskForm(forms.Form):
    text = forms.CharField(label='Task', max_length=200)
    start_date = forms.DateField(label='Start', widget=DateInput(attrs={'type': 'date'}))
    deadline_date = forms.DateField(label='Deadline', widget=DateInput(attrs={'type': 'date'}))