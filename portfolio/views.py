from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


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


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('portfolio:add')

