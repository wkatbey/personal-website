from django.db import models


class BlogEntry(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Title"
    )
    '''primary_image = models.ImageField(
        verbose_name="primary_image"
    )'''
    text_entry = models.CharField(max_length=10000)
    date_of_submission = models.DateTimeField()
    has_been_modified = models.BooleanField(default=False)
    date_updated = models.DateTimeField()

