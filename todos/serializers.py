from todos.models import ToDo
from rest_framework import serializers
from django.contrib.auth.models import User


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username",queryset=User.objects.all())
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ToDo
        fields = [
            "id", "name", "description",  "completed", "user",  "created", "updated"
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'all'


