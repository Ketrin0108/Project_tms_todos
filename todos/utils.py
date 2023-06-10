from django.http import JsonResponse
from .models import ToDo


def todos(request):
    todos_data = [todo for todo in ToDo.objects.all().values('id', 'name', 'description')]
    return JsonResponse({'todos': todos_data})