from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('user:login')
    template_name = 'user/register.html'


class LoginUserView(views.LoginView):
    template_name = 'user/login.html'
    success_url = 'theblog:list'

def logoutUserView(request):
    logout(request)
    return redirect ('user:login')
