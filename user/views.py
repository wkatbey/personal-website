from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

class UserRegistrationView(View):
    def post(self, request):
        user_registration_form = UserCreationForm(request.POST)

        if user_registration_form.is_valid():
            user_registration_form.save()
            username = user_registration_form.cleaned_data.get('username')
            raw_password = user_registration_form.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return HttpResponseRedirect(reverse_lazy('blog:blog-list'))

    def get(self, request):
        user_registration_form = UserCreationForm()
        
        context = {
            'user_registration_form': user_registration_form
        }

        return render(request, 'user/register.html', context)