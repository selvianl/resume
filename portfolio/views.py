from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse


class BaseSudoView(PermissionRequiredMixin, CreateView):
    model = None
    form_class = None
    template_name = None
    success_url = None

    def has_permission(self):
        user = self.request.user
        if user.is_superuser:
            return user.has_perms('portfolio.add')
        raise PermissionDenied


class SignUp(BaseSudoView, CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'

    def get_success_url(self, **kwargs):
        return reverse('portfolio:home:home_index')


