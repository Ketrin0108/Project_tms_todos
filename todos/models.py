
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class ToDo(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


#class Priority(models.Model):
    #name = models.CharField(max_length=50)

   # def __str__(self):
        #return self.name


#class Label(models.Model):
    #name = models.CharField(max_length=50)
   # todos = models.ManyToManyField(ToDo, related_name='labels')

   # def __str__(self):
       # return self.name


# Create your models here.
