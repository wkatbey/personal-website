from django import forms
from django.forms import ModelForm
from blog.models import BlogEntry
from datetime import datetime

'''
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = (
            'title',
        )

        widgets = {
            'title': forms.TextInput
        }
'''

class BlogEntryForm(ModelForm):
    class Meta:
        model = BlogEntry
        fields = (
            'title',
            #'primary_image',
            'text_entry',
            #'category'
        )

        widgets = {
            'text_entry': forms.Textarea(
                attrs = {
                    'cols': 80, 
                    'rows': 20,
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
        }

    def save(self, commit=True):
        blog_instance = super(BlogEntryForm, self).save(commit=False)
        blog_instance.date_of_submission = datetime.now()
        blog_instance.date_updated = datetime.now()

        return blog_instance
