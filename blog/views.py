from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView
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

class CreateBlogView(FormView):
    template_name = 'blog/create-blog.html'
    form_class = BlogForm
    success_url = 'blog/index.html'

    def get_context_data(self, **kwargs):
        data = super(CreateBlogView, self).get_context_data(**kwargs)

        data['blog_form'] = data.get('form')

        return data

    def form_valid(self, form):
        blog_creation_form = form

        if blog_creation_form.is_valid():
            blog_creation_form.save()

        return HttpResponseRedirect(reverse('blog:blog'))