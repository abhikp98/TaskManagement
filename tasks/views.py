from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

from tasks.models import Tasks
from .serialisers import TaskListSerialiser, TaskUpdateSerialiser, TaskCompletionSerialiser

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


class CompletionReport(UpdateAPIView):
    authentication_classes= [JWTAuthentication]
    serializer_class = TaskCompletionSerialiser
    queryset = Tasks.objects.all()
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        stat = self.get_object().status
        if stat == "completed":
            return super().update(request, *args, **kwargs)
        else:
            return Response({"message": "task is not completed"}, status=status.HTTP_403_FORBIDDEN)