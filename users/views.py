
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, DeleteView
from django.views import View
from .models import User
from tasks.models import Tasks, AssignTasks
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
        query = super().get_queryset().filter(role="admin").filter(is_deleted=False)
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
        context = super().get_context_data(**kwargs)
        admin_id = self.kwargs.get("pk")
        context['tasks'] = Tasks.objects.filter(admin=admin_id)
        return context
    

class DeleteAdmins(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        admin_id = self.kwargs.get("pk")
        admin_obj = get_object_or_404(User, id=admin_id)
        admin_obj.is_deleted = True
        admin_obj.save()
        return redirect('manage-admins')
    

class CreateUsers(LoginRequiredMixin, ListView):

    template_name = "super/manage-users.html"
    model = User
    context_object_name = "users"

    def get_queryset(self):
        query = super().get_queryset().filter(role="user").filter(is_deleted=False)
        return query
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            messages.error(request, "Username or email is already exists")
            return render(request, self.template_name)
        
        user = User(username=username, email=email, role="user")
        user.set_password(password)
        user.save()
        messages.success(request, "Added Successfully")
        return redirect('manage-users')

class ViewUsers(LoginRequiredMixin, DetailView):
    template_name = "super/view-user.html"
    model = User
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('pk')
        context['tasks'] = AssignTasks.objects.filter(assigned_to=user_id)
        return context
    

class DeleteUsers(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs.get("pk")
        user_obj = get_object_or_404(User, id=user_id)
        user_obj.is_deleted = True
        user_obj.save()
        return redirect('manage-users')
    


class Managetasks(LoginRequiredMixin, ListView):

    template_name = "admin/manage-tasks.html"
    model = Tasks
    context_object_name = "tasks"

    def get_queryset(self):
        query = super().get_queryset().filter(admin=self.request.user.id).filter(isDeleted=False)
        return query
    
    def post(self, request):
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")

        if Tasks.objects.filter(title=title).exists():
            messages.error(request, "Same Task is already exist")
            return render(request, self.template_name)
        
        task = Tasks(title=title, description=description, due_date=due_date, admin=self.request.user)
        task.save()
        messages.success(request, "Added Successfully")
        return redirect('manage-tasks')


class DeleteTask(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        task_id = self.kwargs.get("pk")
        task_obj = get_object_or_404(Tasks, id=task_id)
        task_obj.is_deleted = True
        task_obj.save()
        return redirect('manage-tasks')

class ViewAssigns(LoginRequiredMixin, ListView):
    model = AssignTasks
    template_name= "admin/view-assigned-tasks.html"
    context_object_name = "assigns"

    def post(self, request, pk):
        task_id = pk
        userid = request.POST.get('userid')
        AssignTasks.objects.create(tasks_id=task_id, assigned_to_id=userid)
        return redirect('manage-tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_id = self.kwargs.get("pk")
        assigned_user_ids = AssignTasks.objects.filter(
            tasks_id=task_id
        ).values_list('assigned_to_id', flat=True)
        unassigned_users = User.objects.filter(role="user").exclude(id__in=assigned_user_ids)
        context['users'] = unassigned_users
        context['task_id'] = task_id
        print(unassigned_users)
        return context

    def get_queryset(self):
        task_id = self.kwargs.get('pk')
        query = super().get_queryset().filter(tasks=task_id)
        return query
    

