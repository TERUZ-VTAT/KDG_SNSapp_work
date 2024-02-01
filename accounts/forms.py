from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import iconPath


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class MailResetForm(forms.Form):
    userid = forms.CharField()
    hashedPass = forms.CharField()
    password = forms.CharField()
    new_mail = forms.EmailField()


class iconForm(ModelForm):
    class Meta:
        model = iconPath
        fields = ('userid', 'filepath')
