# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to="images")    
    body = models.TextField()
    caption = models.CharField(max_length=150)

    # slug field makes a URL more readable
    # EX: if your headline is "Man Saves Baby" slug will turn it into
    # something like https://news.com/man-saves-baby/
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

