from django.shortcuts import render, redirect
from accounts.forms import registerForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.template import RequestContext
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #check if passwords match
        if password == password2:
            if User.objects.filter(username=username).exists():
                print("user exist")
                return redirect('accounts/register.html')
            else:
                if User.objects.filter(email=email).exists():
                    print("email has been used")
                    return redirect('accounts/register.html')
                else:
                    user = User.objects.create_user(username = username, email= email, first_name  = first_name, last_name = last_name,password=password)
                    user.save()
                    return render(RequestContext(request), 'accounts/login.html')
    return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            print("You're loged in\n")
            return render(request, 'accounts/dashboard.html')
        else:
            print("Invalid input\n")

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')