from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('create/', views.CreateBlogView.as_view(), name='create')
]
