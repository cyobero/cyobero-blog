# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from posts.models import Post

# Create your views here.
def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'post': post})

