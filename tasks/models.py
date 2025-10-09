from django.db import models
from users.models import User


class Tasks(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    due_date = models.DateField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField(default=False)
    admin = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class AssignTasks(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    tasks = models.OneToOneField(Tasks, on_delete=models.CASCADE)
    assigned_to = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(default="pending", blank=False, choices=STATUS_CHOICES)
    worked_hours = models.IntegerField(blank=True, null=True)
    completion_report = models.TextField(blank=True, null=True)
