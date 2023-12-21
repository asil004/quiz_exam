from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import TextInput, EmailInput, PasswordInput
from django import forms
from django.urls import reverse_lazy

User = get_user_model()


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            "placeholder": "Enter the password"
        }))
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            "placeholder": "Enter the confirm password"
        }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Enter the first name"
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Enter the last name"
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Enter the username"
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                "placeholder": "Enter the email"
            }),
        }
