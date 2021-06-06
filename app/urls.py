from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('routine/', views.routine, name="routine"),
    path('task/', views.task, name="task"),
]