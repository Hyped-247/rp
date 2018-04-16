from Apt.views import AptListView, CreateApt, UpdateApt, DeleteApt, DetailApt
from django.conf.urls import url

urlpatterns = [
    url(r'^list/(?P<pk>\d+)/$', AptListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>\d+)/$', DetailApt.as_view(), name='detail'),
    url(r'^create/(?P<pk>\d+)/$', CreateApt.as_view(), name='create'),
    url(r'^update/(?P<aptBuilding_pk>\d+)/(?P<pk>\d+)/$', UpdateApt.as_view(), name='update'),
    url(r'^delete/(?P<aptBuilding_pk>\d+)/(?P<pk>\d+)/$', DeleteApt.as_view(), name='delete'),
]
