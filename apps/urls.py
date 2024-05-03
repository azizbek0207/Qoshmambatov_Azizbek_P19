from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from apps.views import InstaRegister, ProfileViewPage

urlpatterns = [
    path('login', LoginView.as_view(
        template_name='apps/index.html',
        redirect_authenticated_user=True,
        next_page='profile'),
        name='insta_page'),
    path('register', InstaRegister.as_view(), name='insta_reg'),
    path('profile/', ProfileViewPage.as_view(), name='profile')
]
