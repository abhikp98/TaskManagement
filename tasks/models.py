from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    assigned_to = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    due_date = models.DateField()
    status = models.CharField(default="pending", blank=False, choices=STATUS_CHOICES)
    worked_hours = models.IntegerField(blank=True, null=True)
    completion_report = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')

    def __str__(self):
        return self.title
