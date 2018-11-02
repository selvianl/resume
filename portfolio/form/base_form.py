from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from portfolio.forms import  HomeForm
from portfolio.models import Home
from django.core.exceptions import PermissionDenied

class BaseFormCreateView(PermissionRequiredMixin, CreateView):
    model = Home
    form_class = HomeForm
    template_name = 'add.html'
    success_url = reverse_lazy('portfolio:home')

    def has_permission(self):
        user = self.request.user
        if user.is_superuser:
            return user.has_perms('portfolio.add')
        raise PermissionDenied