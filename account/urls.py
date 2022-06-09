from django.urls import path
from .views import *

urlpatterns = [
    path('register.html', register, name='register'),
    path('login.html', userLogin, name='userLogin'),
    path('about/<int:id>.html', about, name='about'),
    path('logout.html', userLogout, name='userLogout'),
]