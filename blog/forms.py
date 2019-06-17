from django import forms
from django.forms import ModelForm
from models import BlogEntry

class BlogForm(ModelForm):
    class Meta:
        model = BlogEntry
        fields = [
            'title',
            'primary_image',
            'text_entry'
        ]