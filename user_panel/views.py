from django.shortcuts import render, redirect
from .models import users


def login(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def registerUser(request):
    try:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = users()
        user.email = email
        user.password = password
        if  users.save():
            return redirect('')
            
        print(users.objects.all())
    except Exception as exc:
        print(exc)

    return redirect('register')
    


def dashboard(request):

    try:
        pass
    except Exception as ex:
        print(ex)

    return render(request, 'users/dashboard.html')