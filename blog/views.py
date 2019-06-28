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

class BlogEntryList(ListView):
    model = BlogEntry
    context_object_name = 'blog_entries'
    paginate_by = 100
    
    # In case we need to define new dictionary elements
    # in the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BlogEntryDetailView(DetailView):
    model = BlogEntry
    context_object_name = 'blog_entry'

class BlogEntryCreate(CreateView):
    model = BlogEntry
    form_class = BlogEntryForm

class BlogEntryUpdate(UpdateView):
    model = BlogEntry
    form_class = BlogEntryForm

class BlogEntryDelete(DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog:blog_list')


