from django.db import models

class BlogEntry(models.Model):
    title = models.CharField()
    primary_image = models.ImageField()
    text_entry = models.CharField()
    date_of_submission = models.DateTimeField()
    has_been_modified = models.BooleanField(default=False)
    date_updated = models.DateTimeField()

