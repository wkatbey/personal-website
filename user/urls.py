from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='')),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='')),
]
