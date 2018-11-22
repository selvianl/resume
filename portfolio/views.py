from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from portfolio.models import Home , Works , Skills  ,SkillsCategory


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('portfolio:add')

class CategoryView (ListView):

    template_name = 'skills.html'
    model = SkillsCategory

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        return context

class WorksView(ListView):

    template_name = 'works.html'
    model = Works

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(WorksView, self).get_context_data(**kwargs)
        return context


class HomeView(ListView):
    template_name = 'index.html'
    model = Home

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

class SkillView(ListView):

    template_name = 'skills.html'
    model = Skills

    def get_queryset(self):
        return self.model.objects.filter()

    def get_context_data(self, **kwargs):
        context = super(SkillView, self).get_context_data(**kwargs)
        query_set = SkillsCategory.objects.all()
        context['categories'] = query_set
        return context
