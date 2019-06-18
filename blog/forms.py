from django import forms
from django.forms import ModelForm
from blog.models import BlogEntry

class BlogForm(ModelForm):
    class Meta:
        model = BlogEntry
        fields = (
            'title',
            #'primary_image',
            'text_entry'
        )
