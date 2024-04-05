from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmailForm(forms.Form):
    email_username = forms.CharField(max_length=100)
    email_password = forms.CharField(widget=forms.PasswordInput)


class MassageEmaileForm(forms.Form):
    email_username = forms.CharField(max_length=100)
    email_password = forms.CharField(widget=forms.PasswordInput)
