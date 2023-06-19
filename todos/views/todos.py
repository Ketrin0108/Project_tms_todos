from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from todos.models import ToDo
import requests
import json

from requests import get

def todos(request):  # получение всех todo в json
    todos_data = [todo for todo in ToDo.objects.all().values('id', 'name', 'description')]
    return JsonResponse({'todos': todos_data})


def todo_list(request):  # отображение всех задач в html
    todos = ToDo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def home(request): # создание задачи (Todo) при помощи POST формы
    todos = ToDo.objects.all()
    if request.method == 'GET':
        return render(request, 'todo_list.html', {'todos': todos})
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        user = request.POST.get('user')
        todo = ToDo.objects.create(
            name=name,
            description=description,
            user_id=user
        )
        todos = ToDo.objects.all()
        return redirect('todo_list')
    else:
        return render(request, 'create_todos.html')

def create_todo(request):
    return render(request, "create_todos.html")


# Create your views here



#def get_todo(request, todo_Id:int):
   # todo =next((t for t in Todos().todos if t.todo_id== todo_Id),None)
    #if todo:
     #   return JsonResponse(vars(todo))
    #return HttpResponse(status=404)




# Create your views here.


# Create your views here.
