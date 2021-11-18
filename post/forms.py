from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class PostForm(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['date_added']
        labels = {'title': 'Post Title', 'text': 'Post Discription'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Text'}),
            }


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label= 'Enter Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'autocomplete': 'new-password'}),
        strip=False,
    )
    password2 = forms.CharField(
        label= 'Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'autocomplete': 'new-password'}),
        strip=False,
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Enter Username',
            'first_name': 'Enter First Name',
            'last_name': 'Enter Last Name',
            'email': 'Enter Email',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
        help_text = {'username': 'Enter Username'}
        error_messages = {
            'username': {'required': 'Please Enter Your Username'}
        }
        
        
        
        
class LogInForm(AuthenticationForm):
    username = forms.CharField(
        strip=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus': True})
        )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'autocomplete': 'current-password'}),
    )