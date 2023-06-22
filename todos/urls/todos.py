from django.urls import path

from todos.views.todos import home, todos, todo_list, create_todo, update_todo, delete_todo


urlpatterns = [
    path('', home,name="home"),
    #path('create/', todos.create_todo,name='create_todo'),
    path('todo/', todos,name='todos'),
    path('todo_list/', todo_list, name='todo_list'),
    path('create/',create_todo, name='create_todo'),
    path('update/<int:todo_id>/', update_todo, name='update_todo'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),

]


