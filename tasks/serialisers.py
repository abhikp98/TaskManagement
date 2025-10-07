from rest_framework.serializers import ModelSerializer
from .models import Tasks

class TaskListSerialiser(ModelSerializer):
    models = Tasks
    