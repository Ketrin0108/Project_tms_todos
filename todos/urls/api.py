from django.urls import path

from todos.views.api import todo,todos

urlpatterns = [
    path('', todos),
    path('<int:todo_id>/', todo),

]