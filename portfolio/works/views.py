from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.views.generic import ListView

from portfolio.views import BaseSudoView
from portfolio.works.models import Works
from portfolio.works.forms import WorksForm


class WorksFormView(BaseSudoView):
    model = Works
    form_class = WorksForm
    template_name = 'add_work.html'
    success_url = reverse_lazy('portfolio:works')


class WorksView(ListView):
    template_name = 'works/works.html'
