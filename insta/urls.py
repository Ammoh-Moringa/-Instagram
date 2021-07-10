from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url(r'', views.signup, name='signup'),
    url(r'', include('django.contrib.auth.urls'))
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)