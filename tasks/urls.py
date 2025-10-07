from django.urls import path
from .views import TaskList, TaskUpdate


urlpatterns = [
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('tasks/<int:id>/', TaskUpdate.as_view(), name='task-update'),
    
]