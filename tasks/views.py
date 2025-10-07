from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serialisers import TaskListSerialiser

# Create your views here.
class TaskList(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = TaskListSerialiser