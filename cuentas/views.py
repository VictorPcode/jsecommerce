from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    forms = RegistrationForm()
    context = {
        'forms': forms
    }
    return render(request, 'cuentas/register.html', context)

def login(request):
    return render(request, 'cuentas/login.html')

def logout(request):
    return
