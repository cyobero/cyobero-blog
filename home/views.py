# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from posts.models import Post
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginnator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    # Fetch posts and only display the latest five posts per page.
    # Use pagination to scroll through older posts.
    post_list = get_list_or_404(Post)
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # retrieves first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range then deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'posts': posts})

