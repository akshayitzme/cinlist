from logging import PlaceHolder
from django import forms
from django.contrib.auth.models import User
from .models import List, Movies, Series
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeHolder': 'Username',
            'class': 'mt-3 input w-50 p-2'
        }),
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'mt-3 input w-50 p-2',
                'type': 'email',
                'placeholder': 'Email'
            }),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
                'class': 'mt-3 input w-50 p-2',
                'type': 'password',
                'placeholder': 'Password'
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