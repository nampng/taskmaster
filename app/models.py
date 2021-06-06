from django.db import models
from django.utils import timezone

# Create your models here.

class Routine(models.Model):
    text = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    time = models.TimeField(default=timezone.now)
    last_complete = models.TimeField(default=timezone.now)

class Task(models.Model):
    text = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    start_date = models.DateTimeField(default=timezone.now)
    deadline_date = models.DateTimeField(default=timezone.now)