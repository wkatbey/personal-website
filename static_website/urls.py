from django.contrib import admin
from django.urls import include, path
from . import views 

app_name = 'static_website'
urlpatterns = [
    path('', views.index, name='index'),
    path('resume/', views.resume, name='resume'),
]
