from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserLoginForm(forms.Form):
   email = forms.CharField(
       label='email',
       widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
   password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@gmail.com'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    user_type = forms.ChoiceField(label='User Type', choices=User.USER_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'user_type']

class MahasiswaLoginForm(forms.Form):
   email = forms.CharField(
       label='email',
       widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
   password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
class MahasiswaRegistrationForm(UserCreationForm):
    nim  = forms.IntegerField(label='NIM', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['nim', 'name', 'email', 'password1', 'password2']