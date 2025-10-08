from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('logout/', LogoutView.as_view(next_page="login"),name="logout"),

    #superadmin
    path('manage-admins/', CreateAdmins.as_view(), name="manage-admins"),
    path('manage-admins/<int:pk>/', ViewAdmins.as_view(), name="view-admins"),
    


    
]