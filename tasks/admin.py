from django.contrib import admin
from .models import Tasks, AssignTasks

# Register your models here.
admin.site.register(Tasks)
admin.site.register(AssignTasks)
