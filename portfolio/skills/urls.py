from django.conf.urls import url
from portfolio.skills.views import SkillsView, SkillsFormsView

urlpatterns = [
    url(r'^$', SkillsView.as_view(), name='skill_index'),
    url(r'^add/$', SkillsFormsView.as_view(), name='skill_add'),
]
