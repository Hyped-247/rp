from django.conf.urls import url
from Worker.views import RegisterWorker, ListViewWorker

urlpatterns = [
    url(r'^register/$', RegisterWorker.as_view(), name='register'),
    url(r'^main/$', ListViewWorker.as_view(), name='main'),
]
