from rest_framework import serializers
from .models import Task

class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'task',
             'done',
             )