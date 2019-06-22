from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogEntryList.as_view(), name='blog-list'),
    path('create/', views.BlogEntryCreate.as_view(), name='blog-create'),
    path('update/', views.BlogEntryUpdate.as_view(), name='author-update'),
    path('delete/', views.BlogEntryDelete.as_view(), name='author-delete'),
]
