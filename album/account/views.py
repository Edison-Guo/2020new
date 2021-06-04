from django.shortcuts import render, redirect
from account.forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout



def register(request):
    
    '''
    Register a new user
    '''
    
    template = 'account/register.html'
    
    if request.method == 'GET':
         return render(request, template, {'userForm':UserForm()})
     
    
    # POST    
    userForm = UserForm(request.POST)
    if not userForm.is_valid():
        return render(request, template, {'userForm':UserForm})
    
    userForm.save()
    messages.success(request, '註冊成功')
    return redirect('login')


def login(request):
    '''
    Login an existing user
    '''
    template = 'account/login.html'
    if request.method == 'GET':
        return render(request, template)
    
    #POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:    #Server-side validation
        messages.error(request, '請輸入帳號密碼')
        return render(request, template)
    user = authenticate(username=username, password=password)
    if not user:     #authenticate fails
        messages.error(request, '帳號或密碼不正確')
        return render(request, template)
    
    #login success
    auth_login(request, user)
    nextURL = request.POST.get('nextURL')
    if nextURL:
        return redirect(nextURL)
    messages.success(request, '登入成功')
    return redirect('main:main')


def logout(request):
    '''
    Logout the user
    '''
    
    auth_logout(request)
    messages.success(request, '登出成功')
    return redirect('login')