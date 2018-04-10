from django.contrib.auth.views import LoginView
from django.conf.urls import url
from Owner.views import RegisterOwner

urlpatterns = [
    url(r'^$', RegisterOwner.as_view(), name='owner-main'),
]