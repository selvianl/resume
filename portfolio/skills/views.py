from __future__ import unicode_literals
from django.urls import reverse_lazy

from django.views.generic import ListView

from portfolio.views import BaseSudoView
from portfolio.skills.models import Skills
from portfolio.categories.models import Category
from portfolio.skills.forms import SkillsForm


class SkillsFormsView(BaseSudoView):
    model = Skills
    form_class = SkillsForm
    template_name = 'add_skill.html'
    success_url = reverse_lazy('skills:skills')


class SkillsView(ListView):
    def get_queryset(self):
        return self.model.objects.filter()

    def get_context_data(self, **kwargs):
        context = super(SkillsView, self).get_context_data(**kwargs)
        query_set = Category.objects.all()
        context['categories'] = query_set
        return context
