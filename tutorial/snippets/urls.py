from django.conf.urls import url

from snippets import views

urlpatterns = [
    url(r'^$', views.snippet_list),
]
