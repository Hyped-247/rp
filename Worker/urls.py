from django.conf.urls import url
from Worker.views import RegisterWorker

urlpatterns = [
    url(r'^register/$', RegisterWorker.as_view(), name='register'),
    # url(r'^main/$', OwnerMain.as_view(), name='main'),
]
