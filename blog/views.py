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
from django.contrib.auth.models import User

'''
class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm

class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm

class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = ''
'''

class BlogEntryList(ListView):
    model = BlogEntry
    context_object_name = 'blog_entries'
    
    # In case we need to define new dictionary elements
    # in the context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BlogEntryDetail(DetailView):
    model = BlogEntry
    context_object_name = 'blog_entry'

class BlogEntryCreate(LoginRequiredMixin, CreateView):
    model = BlogEntry
    form_class = BlogEntryForm

    def get_login_url(self):
        login_url = reverse_lazy('user:login')

        return login_url

    def form_valid(self, form):
        blog = form.save()
        blog.author = self.request.user
        blog.save()
        return HttpResponseRedirect(reverse_lazy('blog:blog-detail', kwargs = {
            'pk': blog.id
        }))

class BlogEntryUpdate(LoginRequiredMixin, UpdateView):
    model = BlogEntry
    form_class = BlogEntryForm

    def form_valid(self, form):
        blog = form.save()
        blog.save()
        return HttpResponseRedirect(reverse_lazy('blog:blog-detail', kwargs = {
            'pk': blog.id
        }))

class BlogEntryDelete(LoginRequiredMixin, DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog:blog-list')

class MyPosts(View):
    template_name='blog/user_posts.html'

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        blogs = BlogEntry.objects.all().filter(author=user)

        context = {
            'blogs': blogs,
            'user_viewed': user
        }

        return render(request, self.template_name, context)

