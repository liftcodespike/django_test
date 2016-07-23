from django.conf.urls import url, patterns
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/(?P<id>\d+)/$', views.addPoke),

]
