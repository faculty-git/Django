from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Home
def home(request):
    return render(request,"acc/home.html")

# Registration
def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return redirect('login')
    return render(request,'acc/register.html')

# Login
def login_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid Username or Password")
    return render(request,'acc/login.html')

# Logout
def logout_user(request):
    logout(request)
    return redirect('login')

# Protected Page
@login_required(login_url='login')
def dashboard(request):
    return render(request,'acc/dashboard.html')

# Authorization Example
@login_required(login_url='login')
def admin_page(request):
    if request.user.is_staff:
        return HttpResponse("Welcome Admin/Staff User")
    else:
        return HttpResponse("Access Denied")
