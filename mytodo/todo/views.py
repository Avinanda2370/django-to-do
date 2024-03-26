from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def hello(request):
    var = Todo.objects.all()

    form = TodoFrom()

    if request.method == 'POST':
        form = TodoFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'var': var, 'form': form}
    return render(request, 'todo/index.html', context)


def updatetodo(request, pk):
    var1 = Todo.objects.get(id=pk)

    form = TodoFrom(instance=var1)

    if request.method == 'POST':
        form = TodoFrom(request.POST, instance=var1)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'todo/second.html', context)


def delettodo(request, pk):
    item = Todo.objects.get(id=pk)
    item.delete()


    print(item)
    context = {'item': item}
    return redirect('/')

def deletconfirmation(request,pk):
    item = Todo.objects.get(id=pk)
    context = {'item': item}

    return render(request, 'todo/delete.html',context)
