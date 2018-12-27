# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Home(models.Model):
    header = models.CharField(max_length=50)
    name = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='static/images', blank=True)
