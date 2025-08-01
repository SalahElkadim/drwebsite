from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')