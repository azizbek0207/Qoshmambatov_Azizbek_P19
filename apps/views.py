from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

from apps.forms import RegisterModelForm


# Create your views here.


class InstaRegister(CreateView):
    template_name = 'apps/register.html'
    form_class = RegisterModelForm
    success_url = 'login'


class ProfileViewPage(TemplateView):
    template_name = 'apps/profile.html'
