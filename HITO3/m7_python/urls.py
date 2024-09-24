from django.urls import path
from .views import (indexView, register, register_rol,
                    profile_view, about, contacto, edit_profile_view, profile_exito)

urlpatterns = [
    path('', indexView, name='home'),
    path('accounts/register', register, name='register'),
    path('accounts/register_rol', register_rol, name='register_rol'),
    path('profile', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('profile_exito', profile_exito, name='profile_exito'),
    ###________
    # PATH (routes) SIMPLES
    path('about', about, name='about'),
    path('contacto', contacto, name='contacto'),
    ]