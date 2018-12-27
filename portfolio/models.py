from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
'''
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('add_post', (),
                {'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    name = models.CharField(max_length=42)
    text = models.TextField()
    post = models.ForeignKey(Post,null=True)
    created_at = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.text
'''