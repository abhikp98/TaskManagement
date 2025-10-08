from rest_framework.serializers import ModelSerializer, CharField
from .models import Tasks, AssignTasks, User

class TasksSerializer(ModelSerializer):
    admin = CharField(source='admin.username', read_only=True)

    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'due_date', 'created', 'updated', 'admin']


class TaskListSerialiser(ModelSerializer):
    tasks = TasksSerializer()
    class Meta:
        model = AssignTasks
        exclude = ['assigned_to']
 

class TaskUpdateSerialiser(ModelSerializer):
    class Meta:
        model = AssignTasks
        fields = ['status']


class TaskCompletionSerialiser(ModelSerializer):
    class Meta:
        model = AssignTasks
        fields = ['worked_hours', 'completion_report']
        