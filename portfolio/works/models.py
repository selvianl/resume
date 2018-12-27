from __future__ import unicode_literals
from django.db import models


class Works(models.Model):
    logo = models.ImageField(upload_to="static/images", blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
