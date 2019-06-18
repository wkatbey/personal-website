from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

class IndexView(TemplateView):
    template_name = 'blog/index.html'

class CreateBlogView(View):
     def get(self, request):
        return render(request, 'blog/create-blog.html', {})