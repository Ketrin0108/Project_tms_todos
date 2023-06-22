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


class ToDoListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ToDo
        fields = (
            "id", "name", "description",  "user"
        )
        read_only_fields = ("user")