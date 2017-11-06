from django.conf.urls import url
from ..views.cbv import UserList, UserDetail

urlpatterns = [
    url(r'^$', UserList.as_view(), name='user_list'),
    url(r'^(?P<pk>\d+)/$', UserDetail.as_view(), name='user_detail'),
]