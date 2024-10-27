from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    form_class = CustomUserCreationForm


class UserListView(ListView):
    model = CustomUser
    template_name = "home.html"
