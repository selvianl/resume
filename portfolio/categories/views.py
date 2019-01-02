from __future__ import unicode_literals

from django.urls import reverse_lazy

from portfolio.views import BaseSudoView
from portfolio.categories.models import Category
from portfolio.categories.forms import CategoryForm


class CategoryFormView (BaseSudoView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('portfolio:skill:skill_index')



