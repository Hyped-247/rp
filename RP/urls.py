from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from RP.views import Redirect, Home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^check-user-type/$', Redirect.as_view(), name='check-user-type'),
    url(r'^register/$', TemplateView.as_view(template_name='register.html'), name='register'),

    url(r'^owner/', include('Owner.urls', namespace='owner')),
    url(r'^renter/', include('Renter.urls', namespace='renter')),
    url(r'^worker/', include('Worker.urls', namespace='worker')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
