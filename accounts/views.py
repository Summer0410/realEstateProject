from django.shortcuts import render, redirect
from accounts.forms import registerForm, LoginForm

# Create your views here.
def register(request): 
    form = registerForm 
    return render(request, 'accounts/register.html',{'form': form})
def login(request):
    form = LoginForm
    return render(request, 'accounts/login.html', {'form': form})
def logout(request):
    return redirect('index')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')