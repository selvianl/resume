from django.urls import reverse_lazy
from portfolio.forms import SkillsForm
from portfolio.models import Skills
from portfolio.form import base_form as bf

class SkillsFormView(bf.BaseFormCreateView):

    model = Skills
    form_class = SkillsForm
    template_name = 'add_skill.html'
    success_url = reverse_lazy('portfolio:skills')