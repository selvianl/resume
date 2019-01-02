from django.conf.urls import url
from portfolio.works.views import WorksView, WorksFormView

urlpatterns = [
    url(r'^add/$', WorksFormView.as_view(), name='work_add'),
    url(r'^$', WorksView.as_view(), name='work_index'),
]