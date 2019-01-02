from django.conf.urls import url
from portfolio.home.views import HomeView, HomeFormView

urlpatterns =[
    url(r'^$', HomeView.as_view(), name='home_index'),
    url(r'^add/$', HomeFormView.as_view(), name='home_add'),
]