from Apt.views import AptListView, CreateApt, UpdateApt, DeleteApt
from django.conf.urls import url

urlpatterns = [
    url(r'^detail/(?P<pk>\d+)/$', AptListView.as_view(), name='detail'),
    url(r'^create/(?P<pk>\d+)/$', CreateApt.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/(?P<aptBuilding_pk>\d+)/$', UpdateApt.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/(?P<aptBuilding_pk>\d+)/$', DeleteApt.as_view(), name='delete'),
]
