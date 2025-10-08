from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('dashboard/', dashboard.as_view(), name="dashboard"),
    
]