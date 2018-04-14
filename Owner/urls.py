from django.conf.urls import url, include
from Owner.views import RegisterOwner, ListViewOwner

urlpatterns = [
    url(r'^register/$', RegisterOwner.as_view(), name='register'),
    url(r'^main/$', ListViewOwner.as_view(), name='main'),
    url(r'^aptBuilding/', include('AptBuilding.urls', namespace='apt-building')),
    url(r'^apt/', include('Apt.urls', namespace='apt')),

]
