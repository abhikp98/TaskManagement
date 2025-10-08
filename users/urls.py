from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('logout/', LogoutView.as_view(next_page="login"),name="logout"),

    #superadmin - admin
    path('manage-admins/', CreateAdmins.as_view(), name="manage-admins"),
    path('manage-admins/<int:pk>/', ViewAdmins.as_view(), name="view-admins"),
    path('delete_admin/<int:pk>/', DeleteAdmins.as_view(), name="delete_admin"),

    #Superadmin - user
    path('manage-users/', CreateUsers.as_view(), name="manage-users"),
    path('manage-users/<int:pk>/', ViewUsers.as_view(), name="view-users"),
    path('delete_users/<int:pk>/', DeleteUsers.as_view(), name="delete_users"),
    
]