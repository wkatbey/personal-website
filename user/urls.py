from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'user'
urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='')),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='')),
    path('accounts/change-password/', auth_views.PasswordChangeView.as_view(template_name='')),
    path('accounts/register/', views.UserRegistrationView.as_view(), 'register')
]
