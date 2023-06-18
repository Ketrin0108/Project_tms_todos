from django.urls import path

from . import views


urlpatterns = [
    path('', views.home,name="home"),
    #path('<int:todo_Id>/', views.get_todo),
    path('create/', views.create_todo,name='create_todo'),
    path('ToDo/', views.todos,name='todos'),
    path('todo_list/', views.todo_list, name='todo_list'),

]


