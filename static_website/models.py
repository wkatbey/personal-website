from django.db import models

class PageSectionText(models.Model):
	value = models.TextField()
	col_length = models.IntegerField()

class PageSection(models.Model):
	heading = models.TextField()
	heading_icon = models.TextField()
	text = models.ManyToManyField(PageSectionText)

class HomePage(models.Model):
	intro = models.TextField()

	page_sections = models.ManyToManyField(PageSection)


