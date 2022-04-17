from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name=''),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
]