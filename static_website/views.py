from django.shortcuts import render

def index(request):
    return render(request, 'static_website/index.html', {})

def resume(request):
    return render(request, 'static_website/resume.html', {})