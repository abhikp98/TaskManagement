
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from .models import User
from django.contrib import messages
from django.db.models import Q


class Login(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("dashboard")


class Dashboard(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        role = self.request.user.role
        if  role== "admin":
            self.template_name = "admin/home.html"
        elif role == "superuser":
            self.template_name = "super/home.html"
        else:
            return redirect('login')

        return super().get(request, *args, **kwargs)
    

class CreateAdmins(LoginRequiredMixin, ListView):

    template_name = "super/manage-admins.html"
    model = User
    context_object_name = "admins"

    def get_queryset(self):
        query = super().get_queryset().filter(role="admin")
        return query
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            messages.error(request, "Username or email is already exists")
            return render(request, self.template_name)
        
        user = User(username=username, email=email, role="admin")
        user.set_password(password)
        user.save()
        messages.success(request, "Added Successfully")
        return redirect('manage-admins')

class ViewAdmins(LoginRequiredMixin, DetailView):
    template_name = "super/view-admin.html"
    model = User
    context_object_name = "admin"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    


        