from todos.models import ToDo
from rest_framework import serializers


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = [
            "id", "name", "description",  "completed"
        ]


class ToDoListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ToDo
        fields = (
            "id", "name", "description",  "user"
        )
        read_only_fields = ("user")