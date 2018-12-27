from django.conf.urls import url
from portfolio.categories.views import CategoryView, CategoryFormView

urlpatterns = [
    url(r'^add_category/$', CategoryFormView.as_view(), name='add_category'),
]