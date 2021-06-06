from django.shortcuts import render
from .forms import RoutineForm, TaskForm
from .models import Routine, Task

# Create your views here.
def index(response):
    
    next_routine = GetClosestRoutine()
    next_task = GetClosestTask()

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("done_routine"):
            next_routine.complete = True
            next_routine.save()
            next_routine = GetClosestRoutine()
        elif response.POST.get("done_task"):
            next_task.complete = True
            next_task.save()
            next_task = GetClosestTask()
    return(render(response, 'app/index.html', {"next_routine":next_routine, "next_task":next_task}))

def GetClosestRoutine():
    next_routines = Routine.objects.filter(complete=False).order_by("time")
    next_routine = None

    if next_routines:
        next_routine = next_routines[0]

    return next_routine

def GetClosestTask():
    next_tasks = Task.objects.filter(complete=False).order_by("deadline_date")
    next_task = None
    
    if next_tasks:
        next_task = next_tasks[0]

    return next_task

def routine(response):
    routine_list = Routine.objects.all().order_by("time")
    routine_form = RoutineForm()

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("submit_routine"):
            routine_form = RoutineForm(response.POST)
            if routine_form.is_valid():
                r_text = routine_form.cleaned_data["text"]
                r_time = routine_form.cleaned_data["time"]
                new_routine = Routine(text=r_text, time=r_time)
                new_routine.save()
        elif response.POST.get("save_routine"):
            for routine in routine_list:
                if response.POST.get("c" + str(routine.id)) == "complete":
                    routine.complete = True
                else:
                    routine.complete = False
                routine.save()
        elif response.POST.get("delete_routine"):
            routine_id = int(response.POST.get("delete_routine")[1:])
            routine = Routine.objects.get(id=routine_id)
            routine.delete()


    return(render(response, 'app/routine.html', {'routine_form':routine_form, 'routine_list':routine_list}))

def task(response):
    task_list = Task.objects.all()
    task_form = TaskForm()

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("submit_task"):
            task_form = TaskForm(response.POST)
            if task_form.is_valid():
                t_text = task_form.cleaned_data["text"]
                s_date = task_form.cleaned_data["start_date"]
                d_date = task_form.cleaned_data["deadline_date"]
                new_task = Task(text=t_text, start_date=s_date, deadline_date=d_date)
                new_task.save()
        elif response.POST.get("save_task"):
            for task in task_list:
                if response.POST.get("c" + str(task.id)) == "complete":
                    task.complete = True
                else:
                    task.complete = False
                task.save()
        elif response.POST.get("delete_task"):
            task_id = int(response.POST.get("delete_task")[1:])
            task = Task.objects.get(id=task_id)
            task.delete()


    return(render(response, 'app/task.html', {"task_form":task_form, "task_list":task_list}))