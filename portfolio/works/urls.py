from django.conf.urls import url
from portfolio.works.views import WorksView, WorksFormView

urlpatterns = [
    url(r'^add_work/$', WorksFormView.as_view(), name='add_works'),
    url(r'^works/$', WorksView.as_view(), name='works'),
]