from django.conf.urls import url, include
from .views import view_features, view_feature, create_feature, add_feature_comment, feature_vote

urlpatterns = [
    url(r'^$', view_features, name='view_features'),
    url(r'^(?P<pk>\d+)/$', view_feature, name='view_feature'),
    url(r'^new/$', create_feature, name='create_feature'),
    url(r'^(?P<pk>\d+)/add_feature_comment/$', add_feature_comment, name='add_feature_comment'),
    url(r'^(?P<pk>\d+)/feature_vote/$', feature_vote, name='feature_vote'),
    ]