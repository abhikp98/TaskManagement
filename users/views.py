
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

class Login(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("dashboard")


class dashboard(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        role = self.request.user.role
        if  role== "admin":
            self.template_name = "admin/home.html"
        elif role == "superuser":
            self.template_name = "super/home.html"
        else:
            return redirect('login')

        return super().get(request, *args, **kwargs)
