from rest_framework.serializers import ModelSerializer
from .models import Tasks

class TaskListSerialiser(ModelSerializer):
    class Meta:
        model = Tasks
        exclude = ['assigned_to', 'admin', 'id']
    

class TaskUpdateSerialiser(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['status']


class TaskCompletionSerialiser(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['worked_hours', 'completion_report']
        