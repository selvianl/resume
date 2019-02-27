# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=2222)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
