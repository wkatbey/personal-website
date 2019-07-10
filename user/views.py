from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView

class UserRegistrationView(View):
    def post(self, request):
        user_registration_form = UserCreationForm(request.POST)

        if user_registration_form.is_valid():
            user_registration_form.save()
            username = user_registration_form.cleaned_data.get('username')
            raw_password = user_registration_form.cleaned_data.get('password1')
            
            messages.success(request, f"Congrats, { username }, you've made an account!")
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return HttpResponseRedirect(reverse_lazy('blog:blog-list'))

        context = {
            'user_registration_form': user_registration_form
        }
        
        return render(request, 'user/register.html', context)

    def get(self, request):
        user_registration_form = UserCreationForm()
        
        context = {
            'user_registration_form': user_registration_form
        }

        return render(request, 'user/register.html', context)

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('blog:blog-list')

    def get_success_url(self):
        return success_url

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        
        messages.info(request, 'You are now logged out')
        return HttpResponseRedirect(reverse_lazy('blog:blog-list'))
