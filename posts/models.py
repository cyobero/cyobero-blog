# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to="images")    
    body = models.TextField()
    caption = models.CharField(max_length=150)

    def __unicode__(self):
        return self.title
