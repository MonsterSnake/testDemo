from django.shortcuts import render

def login(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def dashboard(request):

    try:
        pass
    except Exception as ex:
        print(ex)

    return render(request, 'users/dashboard.html')