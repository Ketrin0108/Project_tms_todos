from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from todos.models import ToDo
from rest_framework import viewsets, filters, generics
from rest_framework import permissions
from todos.serializers import ToDoSerializer,UserSerializer

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()  # первые 2 строчки это стандартное отображение команд framework
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated] # классы доступа, обязательное поле AllowAny любым пользователям
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter]
    ordering_fields = ['id', 'name', 'created'] # поля по которым мы хотим сортиировать
    filterset_fields = ['name'] # фильтр по полям
    search_fields = ['name'] # поиск по ...


