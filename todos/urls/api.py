from django.urls import path

from todos.views.api import todo,todos

urlpatterns = [
    path('', todos, name="api-todos"),
    path('<int:todo_id>/', todo),

]