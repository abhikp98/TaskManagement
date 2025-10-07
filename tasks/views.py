from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from tasks.models import Tasks
from .serialisers import TaskListSerialiser, TaskUpdateSerialiser

# Create your views here.
class TaskList(ListAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = TaskListSerialiser
    queryset = Tasks.objects.all()

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(assigned_to=self.request.user.id)
    

class TaskUpdate(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = TaskUpdateSerialiser
    queryset = Tasks.objects.all()
    lookup_field = 'id'
