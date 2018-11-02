from django.conf.urls import url , include
from portfolio.form import base_form ,skills_form ,works_form, category_form
from portfolio.views import *


urlpatterns = [
    url(r'^add/$', base_form.BaseFormCreateView.as_view(), name='add_home'),
    url(r'^add_work/$', works_form.WorksFormView.as_view(), name='add_works'),
    url(r'^add_skill/$', skills_form.SkillsFormView.as_view(), name='add_skills'),
    url(r'^add_category/$', category_form.SkillCategoryFromView.as_view(), name='add_category'),


    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^works/$', WorksView.as_view(), name='works'),
    url(r'^skill/$', SkillView.as_view(), name='skills'),
    url(r'^skill/$', CategoryView.as_view(), name='category'),

]
