from AptBuilding.views import CreateAptBuilding, UpdateAptBuilding, DeleteAptBuilding, DetailAptBuilding
from django.conf.urls import url

urlpatterns = [
    url(r'^create/$', CreateAptBuilding.as_view(), name='create'),
    url(r'^detail/(?P<pk>\d+)/$', DetailAptBuilding.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', UpdateAptBuilding.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteAptBuilding.as_view(), name='delete'),
]

