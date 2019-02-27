from django.conf.urls import url, include

urlpatterns = [

    url(r'^work/', include('portfolio.works.urls', namespace='work')),
    url(r'^blog/', include('portfolio.blog.urls', namespace='blog')),
    url(r'^skill/', include('portfolio.skills.urls', namespace='skill')),
    url(r'^category/', include('portfolio.categories.urls', namespace='category')),
    url(r'^', include('portfolio.home.urls', namespace='home')),


]
