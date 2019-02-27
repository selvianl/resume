from django.conf.urls import url
from portfolio.blog.views import BlogFormView, BlogView

urlpatterns = [
    url(r'^add/$', BlogFormView.as_view(), name='blog_add'),
    url(r'^$', BlogView.as_view(), name='blog_index'),

]