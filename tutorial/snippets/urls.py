from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.snippet_list, name='snippets'),
    url(r'^(?P<pk>\d+)/$', views.snippet_detail, name='snippet_detail'),
]
