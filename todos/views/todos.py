from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.db.models import F
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page

from todos.models import ToDo
from todos.forms import ToDoForm,ToDoUpdateForm
import requests
import json

from requests import get
@cache_page(60 * 15)
def todos(request):
    return render(request, "todos.html", {"todos": ToDo.objects.select_related("user").all()})

def todo_list(request):  # отображение всех задач в html
    todos = ToDo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, "create_todo.html", {"form": form})

    return render(request, "create_todo.html", {"form": ToDoForm()})


def update_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    form = ToDoUpdateForm(instance=todo)
    if request.method == "POST":
        form = ToDoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
    return render(request, "update_todo.html", {"form": form})


def delete_todo(request, todo_id):
    if request.method == "POST":
        ToDo.objects.get(id=todo_id).delete()
        return redirect("todo_list")



# Create your views here








# Create your views here.


# Create your views here.
