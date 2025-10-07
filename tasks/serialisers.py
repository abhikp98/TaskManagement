from rest_framework.serializers import ModelSerializer
from .models import Tasks

class TaskListSerialiser(ModelSerializer):
    class Meta:
        model = Tasks
        exclude = ['assigned_to', 'admin', 'id']


    