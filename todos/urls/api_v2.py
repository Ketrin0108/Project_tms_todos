from django.urls import include, path
from rest_framework import routers
from todos.views.api_v2 import ToDoViewSet

router = routers.DefaultRouter()
router.register('todo', ToDoViewSet)

urlpatterns = [
    path('', include(router.urls)),

]