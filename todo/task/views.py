from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    task = Task.objects.all()

    form = taskForm()

    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'task': task, 'form': form }
    return render(request, 'task/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = taskForm(instance=task)

    context = {'form': form}

    return render(request, "task/update_task.html")