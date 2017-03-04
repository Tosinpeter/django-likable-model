#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin
from like.models import Like


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'object_id', 'content_object')

admin.site.register(Like, LikeAdmin)
