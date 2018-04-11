from django.conf.urls import url
from Owner.views import RegisterOwner, OwnerMain

urlpatterns = [
    url(r'^register/$', RegisterOwner.as_view(), name='register'),
    url(r'^main/$', OwnerMain.as_view(), name='main'),
]
