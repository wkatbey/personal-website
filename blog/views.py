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
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogEntryList(ListView):
    model = BlogEntry
    context_object_name = 'blog_entries'
    paginate_by = 7
    
    # In case we need to define new dictionary elements
    # in the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BlogEntryDetailView(DetailView):
    model = BlogEntry
    context_object_name = 'blog_entry'

class BlogEntryCreate(LoginRequiredMixin, CreateView):
    model = BlogEntry
    form_class = BlogEntryForm

    def get_login_url(self):
        login_url = reverse_lazy('user:login')

        return login_url

class BlogEntryUpdate(LoginRequiredMixin, UpdateView):
    model = BlogEntry
    form_class = BlogEntryForm

class BlogEntryDelete(LoginRequiredMixin, DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog:blog-list')


