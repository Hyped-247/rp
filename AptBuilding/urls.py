from AptBuilding.views import CreateAptBuilding, UpdateAptBuilding, DeleteAptBuilding
from django.conf.urls import url

urlpatterns = [
    url(r'^create/$', CreateAptBuilding.as_view(), name='create'),
    url(r'^update/$', UpdateAptBuilding.as_view(), name='update'),
    url(r'^delete/$', DeleteAptBuilding.as_view(), name='delete'),
]
