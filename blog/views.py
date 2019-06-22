from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from blog.forms import BlogForm

class IndexView(TemplateView):
    template_name = 'blog/index.html'

class CreateBlogView(View):
    def get(self, request):
        blog_creation_form = BlogForm()
        context = {
            'blog_creation_form': blog_creation_form
        }
        return render(request, 'blog/create-blog.html', context)

    def post(self, request):
        return render(request, 'blog/create-blog.html', {})
