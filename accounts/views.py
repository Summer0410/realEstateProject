from django.shortcuts import render, redirect
from accounts.forms import registerForm, LoginForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        print("It worked")
    return render(request, 'accounts/register.html')
def login(request):
    return render(request, 'accounts/login.html')
def logout(request):
    return redirect('index')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')