from django.conf.urls import url
from Owner.views import RegisterOwner, ListViewOwner

urlpatterns = [
    url(r'^create/$', RegisterOwner.as_view(), name='create'),
    url(r'^update/$', RegisterOwner.as_view(), name='update'),
    url(r'^delete/$', RegisterOwner.as_view(), name='delete'),
]
