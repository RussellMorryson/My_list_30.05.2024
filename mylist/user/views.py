#import os
from django.shortcuts import redirect, render
from .forms import LoginUserForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
#from django.core.files.storage import FileSystemStorage

def login_user(request):    
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])            
            if user and user.is_active:
                login(request, user)
                pro = redirect('index')
                username = str(user.get_username())
                pro.set_cookie('username', username)
                return pro
    else:
        form = LoginUserForm()
    return render(request, 'user/login.html', {'form': form})

def logout_user(request):
    response = redirect('login_user')
    logout(request)
    if request.COOKIES.get('username'):
        response.delete_cookie("username")
    return response
    
    
    # response.delete_cookie("username")
    # global username
    # username = ''
    # logout(request)
    # form = LoginUserForm()
    # return render(request, 'user/login.html', {'form': form})
def regist_user(request):    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            form = LoginUserForm()
            return render(request, 'user/login.html', {'form': form})
    else:
        form = CreateUserForm()
    return render(request, 'user/registration.html', {'form': form})