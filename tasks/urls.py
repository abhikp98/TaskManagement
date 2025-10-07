from django.urls import path
from .views import TaskList, TaskUpdate, CompletionReport


urlpatterns = [
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('tasks/<int:id>/', TaskUpdate.as_view(), name='task-update'),
    path('task-completion/<int:id>/', CompletionReport.as_view(), name='task-completion'),

]