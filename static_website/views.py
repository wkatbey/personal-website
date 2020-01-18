from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from static_website.forms import ContactForm
from django.core.mail import send_mail
from .models import *
from .tools.mapping import *
from .seed_data.home_page import get_default_home_page

COMPANY_EMAIL = 'katbeywassim@gmail.com'
DEFAULT_SUBJECT = 'Website Email'

class Home(View):
    template_name = 'static_website/index.html'

    def get(self, request):
        form = ContactForm()

        # Retrieve the introduction text from the 
        # database
        home_page_model = HomePage.objects.all().first()

        if not home_page_model:
            print("No home page")
            home_page = get_default_home_page()
            home_page.save()
        else:
            home_page = construct_home_page_from_model(home_page_model)

        context = {
            'home_page': home_page,
            'form': form,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        context = {}
        form = ContactForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data['inquiry']
            from_email = form.cleaned_data['email']
            full_name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
            subject = full_name + ': ' + DEFAULT_SUBJECT

            send_mail(subject, message, from_email, [COMPANY_EMAIL], fail_silently=True)
     
            form = ContactForm()

            context['form'] = form
            context['message'] = "I appreciate your email! I'll get back to you as soon as I can!"

            return redirect(request.path)

        form = ContactForm()
        return redirect(request.path)

def resume(request):
    return render(request, 'static_website/resume.html', {})


