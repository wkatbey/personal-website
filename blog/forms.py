from django import forms
from django.forms import ModelForm
from blog.models import BlogEntry
from datetime import datetime

class BlogForm(ModelForm):
    class Meta:
        model = BlogEntry
        fields = (
            'title',
            #'primary_image',
            'text_entry'
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
            )
        }

    def save(self, commit=True):
        instance = super(BlogForm, self).save(commit=False)
        instance.date_of_submission = datetime.now()
        instance.date_updated = datetime.now()

        if commit:
            instance.save()
        
        return instance
