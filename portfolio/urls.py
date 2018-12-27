from django.conf.urls import url, include

urlpatterns = [

    url(r'^work/', include('portfolio.works.urls', namespace='work')),
    url(r'^skill/', include('portfolio.skills.urls', namespace='skill')),
    url(r'^category/', include('portfolio.categories.urls', namespace='category')),
    url(r'^home/', include('portfolio.home.urls')),

]
