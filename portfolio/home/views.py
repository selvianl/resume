from django.urls import reverse_lazy
from django.views.generic import ListView

from portfolio.views import BaseSudoView
from portfolio.home.forms import HomeForm
from .models import Home
from django.core.exceptions import PermissionDenied


class HomeFormView(BaseSudoView):
    model = Home
    form_class = HomeForm
    template_name = 'home_add.html'
    success_url = reverse_lazy('portfolio:home:home_index')

    def has_permission(self):
        user = self.request.user
        if user.is_superuser:
            return user.has_perms('portfolio.add')
        raise PermissionDenied


class HomeView(ListView):
    template_name = 'home_index.html'

    def get_queryset(self):
        return Home.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['objects'] = Home.objects.all()
        return context



