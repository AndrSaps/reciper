from django import forms

from django.contrib.auth.models import User
from .models import Comments, ServiseUser

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ServiceUserForm(forms.ModelForm):
    class Meta:
        model = ServiseUser
        fields = ('photo',)