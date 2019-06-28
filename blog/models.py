from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse, reverse_lazy


class BlogEntry(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Title"
    )
    '''primary_image = models.ImageField(
        verbose_name="primary_image"
    )'''
    text_entry = HTMLField()
    date_of_submission = models.DateTimeField()
    has_been_modified = models.BooleanField(default=False)
    date_updated = models.DateTimeField(default=None)

    def get_absolute_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.pk})
