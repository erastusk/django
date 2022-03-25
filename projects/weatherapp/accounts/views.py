from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.middleware.csrf import get_token
from django.contrib.auth import login, logout, user_logged_in, user_logged_out
from django.contrib import messages

def signup(request):
    csrf_token = get_token(request)
    if request.method == 'POST':        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.SUCCESS(request, 'Account created successfully')            
            return redirect('accounts:signin')
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def signin(request):
    csrf_token = get_token(request)
    if request.method == 'POST':        
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() 
            if user:
                login(request,user)                           
                return redirect('userprofile:profile', user.id)
    form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form':form})

def signout(request):
    csrf_token = get_token(request)
    if request.method == 'POST':
        logout(request)            
        return redirect('home')    
    return redirect('home')            
