from django.conf.urls import url , include
from portfolio.views import *


urlpatterns = [
    url(r'^add/$', BaseFormCreateView.as_view(), name='add_home'),
    url(r'^add_work/$', WorksFormView.as_view(), name='add_works'),
    url(r'^add_skill/$', SkillsFormView.as_view(), name='add_skills'),


    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^works/$', WorksView.as_view(), name='works'),
    url(r'^skill/$', SkillView.as_view(), name='skills')

]
