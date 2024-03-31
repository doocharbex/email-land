from django import forms


class EmailForm(forms.Form):
    email_username = forms.CharField(max_length=100)
    email_password = forms.CharField(widget=forms.PasswordInput)


class MassageEmaileForm(forms.Form):
    email_username = forms.CharField(max_length=100)
    email_password = forms.CharField(widget=forms.PasswordInput)