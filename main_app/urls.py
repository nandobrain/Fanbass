from django.urls import path
from . import views


path('accounts/signup/', views.signup, name='signup'),