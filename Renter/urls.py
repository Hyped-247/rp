from django.conf.urls import url
from Renter.views import RegisterRenter, ListViewRenter

urlpatterns = [
    url(r'^register/$', RegisterRenter.as_view(), name='register'),
    url(r'^main/$', ListViewRenter.as_view(), name='main'),
]
