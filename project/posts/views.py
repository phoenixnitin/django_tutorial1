# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.
def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("phonenumber")
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	# if request.method == "POST":
	# 	print request.POST.get("content")
	# 	title = request.POST.get("title")
	# 	content = request.POST.get("content")
	# 	Post.objects.create(title=title, content=content)
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)
	# return HttpResponse('<h1>Create</h1>')

def post_detail(request, id=None):
	# instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id=id )#title__icontains='some')
	context = {
		"title": "Detail",
		"day": "Sunday",
		"instance": instance,
	}

	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "Detail",
	# 		"day": "Sunday"
	# 	}
	# else:
	# 	context = {
	# 		"title": "Detail for unauthenticated",
	# 		"day": "Friday"
	# 	}
	return render(request, "post_detail.html", context)
	# return HttpResponse('<h1>Detail</h1>')

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"title": "List",
		"day": "Monday",
		"object_list" : queryset
	}
	return render(request, "index.html", context)
	# return HttpResponse('<h1>List</h1>')

def post_update(request, id):
	# return HttpResponse('<h1>Update</h1>')
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=True)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": "Detail",
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)


def post_delete(request):
	return HttpResponse('<h1>Delete</h1>')