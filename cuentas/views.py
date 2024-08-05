from django.shortcuts import render

def register(request):
    return render(request, 'cuentas/register.html')

def login(request):
    return render(request, 'cuentas/login.html')

def logout(request):
    return
