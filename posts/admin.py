# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from posts.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
