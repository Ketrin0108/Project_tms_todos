from django.http import JsonResponse
from django.shortcuts import render,redirect

from .models import ToDo


def todos(request): # получение всех todo в json
    todos_data = [todo for todo in ToDo.objects.all().values('id', 'name', 'description')]
    return JsonResponse({'todos': todos_data})

def todo_list(request): # отображение всех задач в html
    todos = ToDo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

# ToDo.objects.all() -получение всех постов

# ToDo.objects.values('id','name') -получение только id и name у поста

# ToDo.objects.get(id=1) -получение поста по id

# ToDo.objects.select_related('user').get(id=1) -получение поста и его юзера

# ToDo.objects.filter(name__contains="go to") -получение поста по части названия (аналог LIKE в SQL)



def home(request):
    todos = ToDo.objects.all()
    if request.method == 'GET':
        return render(request, 'todo_list.html', {'todos': todos})
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        user = request.POST.get('user_id')
        todo = ToDo.objects.create(
            name=name,
            description=description,
            user=user
        )
        todos.append(todo)
        return redirect('todo_list')
    else:
        return render(request, 'create_todo.html')

def create_todo(request):
    return render(request, "create_todo.html")


