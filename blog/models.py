from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.contrib.auth.models import User

'''
class Category(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Categories"
    )

    description = models.CharField(
        max_length=500,
        verbose_name="Description"
    )
'''

class BlogEntry(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Title"
    )

    #primary_image = models.ImageField(verbose_name="Primary Image")
    text_entry = HTMLField()
    date_of_submission = models.DateTimeField()
    has_been_modified = models.BooleanField(default=False)
    date_updated = models.DateTimeField(default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    #category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=[self.id])
