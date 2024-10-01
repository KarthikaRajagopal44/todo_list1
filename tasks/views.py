from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form= TaskForm()
    if request.method=='POST':
        form =TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {"tasks":tasks, "form":form}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'tsks/update_task.html')