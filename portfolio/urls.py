from django.conf.urls import url , include
from portfolio.views import *


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^add/$', HomeCreate.as_view(), name='add'),

]
