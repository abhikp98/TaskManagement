from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    assigned_to = models.OneToOneField(User, on_delete=models.CASCADE)
    due_date = models.DateField()
    status = models.CharField(default="p", blank=False)
    worked_hours = models.IntegerField()
    completion_report = models.TextField
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

