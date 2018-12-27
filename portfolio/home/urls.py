from django.conf.urls import url
from portfolio.home.views import HomeView

urlpatterns =[
    url(r'^add/$', HomeView.as_view(), name='add_home')
]