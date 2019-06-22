from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from blog.forms import BlogForm
from blog.models import BlogEntry
from django.urls import reverse

class IndexView(View):

    def get(self, request):
        blogs = BlogEntry.objects.all()

        context = {
            'blogs': blogs
        }
        
        return render(request, 'blog/index.html', context)

class CreateBlogView(View):
    def get(self, request):
        blog_creation_form = BlogForm()
        context = {
            'blog_creation_form': blog_creation_form
        }
        return render(request, 'blog/create-blog.html', context)

    def post(self, request):
        blog_creation_form = BlogForm(request.POST)

        if blog_creation_form.is_valid():
            blog_creation_form.save()

        return HttpResponseRedirect(reverse('blog:blog'))