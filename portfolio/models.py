from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


class Home(models.Model):
    id = models.AutoField(primary_key=True)
    header = models.CharField(max_length=50)
    name = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='static/images', blank=True)

    def get_absolute_url(self):
        return reverse('show', kwargs={'id': self.id})



class Works(models.Model):
    id = models.AutoField(primary_key=True)
    logo = models.ImageField(upload_to="static/images", blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)



class SkillsCategory (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Skills(models.Model):
    id = models.AutoField(primary_key=True, default="Languages", editable=True)
    category = models.ForeignKey('SkillsCategory', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='static/images', blank=True)



class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)




class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    blog = models.TextField()
    post = models.ForeignKey(Blog)

    class Meta:
        unique_together = ('post', "blog")
