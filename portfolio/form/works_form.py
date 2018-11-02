from django.urls import reverse_lazy
from portfolio.forms import WorksForm
from portfolio.models import Works
from portfolio.form import base_form as bf


class WorksFormView(bf.BaseFormCreateView):
    model = Works
    form_class = WorksForm
    template_name = 'add_work.html'
    success_url = reverse_lazy('portfolio:works')