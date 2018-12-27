from django.conf.urls import url
from portfolio.skills.views import SkillsView, SkillsFormsView

urlpatterns = [
    url(r'^add_skill/$', SkillsFormsView.as_view(), name='add_skills'),
    url(r'^skill/$', SkillsView.as_view(), name='skills'),
]
