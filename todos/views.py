from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import requests
import json



# Create your views here

RESPONSE = requests.get("https://jsonplaceholder.typicode.com/todos").json()
URL="https://jsonplaceholder.typicode.com/todos"

class Todo:
    def __init__(self, todo_id, user_id, title, completed):
        self.todo_id = todo_id
        self.user_id = user_id
        self.title = title
        self.completed = completed

    def __str__(self):
        return f"Todo: {self.todo_id}, User: {self.user_id}, Title: {self.title}, Completed: {self.completed}"


class Todos:
    def __init__(self):
        self.todos = []
        for todo in requests.get(URL).json():
            self.todos.append(Todo(todo['id'], todo['userId'], todo['title'], todo['completed']))
        self.current = 0

    def __len__(self):
        return len(self.todos)

    def __iter__(self): # иттератор
        return iter(self.todos)

    def __next__(self):
        if self.current < len(self.todos):
            todo = self.todos[self.current]
            self.current += 1
            return todo
        else:
            raise StopIteration

    def get_todo_by_id (self, todo_id): # возможность на todo по id
        for todo in self.todos:
            if todo.todo_id == todo_id:
                return todo
        return None

    def to_dict(self):
        return [todo.__dict__ for todo in self.todos]

    def from_dict(self, todos_data):
        self.todos = []
        for todo_data in todos_data:
            todo = Todo(
                todo_data['id'],
                todo_data['userId'],
                todo_data['title'],
                todo_data['completed']
            )
            self.todos.append(todo)

    def save_json(self, file_name):
        with open(file_name, 'w') as f:
            json.dump(self.to_dict(), f)

    def load_json(self, file_name):
        with open(file_name, 'r') as f:
            todos_data = json.load(f)
            self.from_dict(todos_data)

#def home(request):       # обработка GET ЗАПРОСА
    #return render(request, 'todos.html', {'todos': requests.get(URL).json()})

def home(request):
    if request.method == 'GET':
        return render(request, 'todos.html', {'todos': requests.get(URL).json()})

    elif request.method == 'POST':
        todo_ = dict(request.POST)
        for key in todo_:
            todo_[key] = todo_[key][0]

        todo_["id"] = int(todo_["id"]) if "id" in todo_ else 5
        Todos().todos.append(todo_)
        return render(request,'todos.html', {'todos':requests.get(URL).json()})

def create_todo(request):
    return render(request, "create_todo.html")

def todo(request):
    return JsonResponse({'todos': RESPONSE})

def get_todo(request, todo_Id:int):
    todo =next((t for t in Todos().todos if t.todo_id== todo_Id),None)
    if todo:
        return JsonResponse(vars(todo))
    return HttpResponse(status=404)




# Create your views here.


# Create your views here.
