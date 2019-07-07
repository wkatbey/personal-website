from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse, reverse_lazy
from django.conf import settings


class BlogEntry(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Title"
    )
    text_entry = HTMLField()
    date_of_submission = models.DateTimeField()
    has_been_modified = models.BooleanField(default=False)
    date_updated = models.DateTimeField(default=None)

    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=[self.id])
