from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from portfolio.forms import HomeForm
from portfolio.models import Home
from django.core.exceptions import PermissionDenied


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class HomeCreate(PermissionRequiredMixin, CreateView):
    model = Home
    form_class = HomeForm
    template_name = 'add.html'
    success_url = reverse_lazy('portfolio:home')

    def has_permission(self):
        user = self.request.user
        if user.is_superuser:
            return user.has_perms('portfolio.add')
        raise PermissionDenied

    def get_queryset(self):
        return self.model.objects.get.latest(id=self.kwargs.get("id"))

    def get_context_data(self, **kwargs):
        context = super(HomeCreate, self).get_context_data(**kwargs)
        return context


class ShowView(ListView):
    template_name = 'show.html'
    model = Home

    def get_queryset(self):
        return self.model.objects.latest("id")

    def get_context_data(self, **kwargs):
        context = super(ShowView, self).get_context_data(**kwargs)
        return context


class HomeView(ListView):
    template_name = 'index.html'
    model = Home

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

def add(request):
    return render(request, 'demo.html')



#add_view = login_required(HomeCreate.as_view())