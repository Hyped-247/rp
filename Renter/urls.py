from django.conf.urls import url
from Renter.views import RegisterRenter

urlpatterns = [
    url(r'^register/$', RegisterRenter.as_view(), name='register'),
    #url(r'^main/$', OwnerMain.as_view(), name='main'),
]
