from todos.models import ToDo
from rest_framework import serializers
from django.contrib.auth.models import User


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username",queryset=User.objects.all())
    class Meta:
        model = ToDo
        fields = [
            "id", "name", "description",  "completed", "user"
        ]


