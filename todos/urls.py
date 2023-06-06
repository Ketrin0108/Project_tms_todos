from django.urls import path

from . import views
from .utils import todos

urlpatterns = [
    path('/', views.home,name="home"),
    path('/todo/', views.todo,name="todo"),
    path('/<int:todo_Id>/', views.get_todo),
    path('/create/', views.create_todo),
    path('//', todos),

]
