from django.http import JsonResponse
from django.shortcuts import render,redirect

from .models import ToDo


# ToDo.objects.all() -получение всех постов

# ToDo.objects.values('id','name') -получение только id и name у поста

# ToDo.objects.get(id=1) -получение поста по id

# ToDo.objects.select_related('user').get(id=1) -получение поста и его юзера

# ToDo.objects.filter(name__contains="go to") -получение поста по части названия (аналог LIKE в SQL)




