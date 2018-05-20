from django.conf.urls import url, include
from .views import view_bugs, view_bug, create_bug, add_comment

urlpatterns = [
    url(r'^$', view_bugs, name='view_bugs'),
    url(r'^(?P<pk>\d+)/$', view_bug, name='view_bug'),
    url(r'^new/$', create_bug, name='create_bug'),
    url(r'^(?P<pk>\d+)/add_comment/$', add_comment, name='add_comment'),
    ]