from __future__ import unicode_literals

from django.db import models


class Skills(models.Model):
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='static/images', blank=True)
