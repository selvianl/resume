from django.urls import reverse_lazy
from portfolio.views import BaseSudoView
from portfolio.home.forms import HomeForm
from .models import Home
from django.core.exceptions import PermissionDenied


class HomeView(BaseSudoView):
    model = Home
    form_class = HomeForm
    template_name = 'add_home.html'
    success_url = reverse_lazy('portfolio:home')

    def has_permission(self):
        user = self.request.user
        if user.is_superuser:
            return user.has_perms('portfolio.add')
        raise PermissionDenied
