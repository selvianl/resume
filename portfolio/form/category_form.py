from django.urls import reverse_lazy
from portfolio.forms import SkillsCategoryForm
from portfolio.models import SkillsCategory
from portfolio.form import base_form as bf

class SkillCategoryFromView (bf.BaseFormCreateView):

    model = SkillsCategory
    form_class = SkillsCategoryForm
    template_name = 'add_category.html'
    success_url = reverse_lazy('portfolio:category')