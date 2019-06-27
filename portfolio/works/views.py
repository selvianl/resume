from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.views.generic import ListView

from portfolio.views import BaseSudoView
from portfolio.works.models import Works
from portfolio.works.forms import WorksForm


class WorksFormView(BaseSudoView):
    model = Works
    form_class = WorksForm
    template_name = 'work_add.html'
    success_url = reverse_lazy('portfolio:work:work_index')


class WorksView(ListView):
    template_name = 'work_index.html'

    def get_queryset(self):
        return Works.objects.all()

    def get_context_data(self, **kwargs):
        context = super(WorksView, self).get_context_data(**kwargs)
        context['objects'] = Works.objects.all()
        return context
