from django.forms import models
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 128)
    password = forms.CharField(widget = forms.PasswordInput(), max_length = 128)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        user = authenticate(**self.cleaned_data)
        if user:
            login(self.request, user)
        else:
            raise ValidationError('Incorrect login/password')
        return self.cleaned_data


class RegisterForm(models.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(), max_length = 128)
    password_confirmation = forms.CharField(widget = forms.PasswordInput(), max_length = 128)

    def clean_password_confirmation(self):
        if self.cleaned_data.get('password_confirmation') != self.cleaned_data.get('password'):
            raise ValidationError('Passwords didn''t match')
        return self.cleaned_data['password_confirmation']
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation')
