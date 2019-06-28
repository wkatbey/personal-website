from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from blog.forms import BlogEntryForm
from blog.models import BlogEntry
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

class UserRegistrationView(View):
    def post(self, request):
        pass
