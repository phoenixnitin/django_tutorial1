# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Post

from django.contrib import admin

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "content", "timestamp", "updated"]
	list_display_links = ['updated']
	list_filter = ["updated", "timestamp", "title"]
	search_fields = ["title", "content"]
	list_editable = ["title"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)