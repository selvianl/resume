from django.conf.urls import url
from portfolio.categories.views import CategoryFormView

urlpatterns = [
    url(r'^add/$', CategoryFormView.as_view(), name='category_add'),
]