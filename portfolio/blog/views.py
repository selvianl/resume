# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.views.generic import ListView

from portfolio.blog.models import Blog
from portfolio.blog.forms import BlogForm
from portfolio.views import BaseSudoView


class BlogFormView(BaseSudoView):
    model = Blog
    form_class = BlogForm
    template_name = 'post_add.html'
    success_url = reverse_lazy('portfolio:blog:blog_index')


class BlogView(ListView):
    template_name = 'post_index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Blog.objects.filter(user=self.request.user)
        return

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['objects'] = Blog.objects.all()
        return context
