from django.urls import path

from todos.views import todos


urlpatterns = [
    path('', todos.home,name="home"),
    path('create/', todos.create_todo,name='create_todo'),
    path('ToDo/', todos.todos,name='todos'),
    path('todo_list/', todos.todo_list, name='todo_list'),

]


