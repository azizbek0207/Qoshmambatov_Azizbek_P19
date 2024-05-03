from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class RegisterModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'username']

    def clean_password(self):
        return make_password(self.cleaned_data.get('password'))

