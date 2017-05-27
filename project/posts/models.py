# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	phonenumber = PhoneNumberField(blank=True)

	def __unicode__(self):
		return self.title + ' - ' + self.content

	def __str__(self):
		return self.title +  ' - ' + self.content

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})
		# return "/posts/%s/" %(self.id)