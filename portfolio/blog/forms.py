from portfolio.blog.models import Blog
from django import forms
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
