from django import forms
from django.contrib.auth.models import User
from .models import List, Movies, Series
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            
        }),
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                
            }),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            
        }),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            
        }),
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class NewMovieForm(forms.Form):
    pass

class NewSeriesForm(forms.Form):
    pass

class NewListForm(forms.Form):
    pass