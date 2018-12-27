from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.views.generic import ListView

from portfolio.views import BaseSudoView
from portfolio.categories.models import Category
from portfolio.categories.forms import CategoryForm


class CategoryFormView (BaseSudoView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'
    success_url = reverse_lazy('categories:category')


class CategoryView (ListView):
    template_name = 'skills/skills.html'


