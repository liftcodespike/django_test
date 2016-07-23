from django.conf.urls import url, patterns
from . import views


urlpatterns = [
    url(r'^$', views.direct, name = 'direct'),
    url(r'^main/$', views.main, name = 'main'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^logout/$', views.logout, name = 'logout'),
    ]

