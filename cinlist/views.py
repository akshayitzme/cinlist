from django.shortcuts import render, redirect
from .forms import SignUpForm, NewListForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or Password is incorrect')

    return render(request, 'signin.html')


def signoutUser(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data
            messages.success(request, "Account was created for " + user['username'])
            return redirect('signin')
    context = {'form': form}

    return render(request, 'signup.html', context)
