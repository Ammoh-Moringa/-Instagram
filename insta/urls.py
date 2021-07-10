from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns=[
    url(r'', views.signup, name='signup'),
    url(r'', include('django.contrib.auth.urls')),
    url('login/',auth_views.LoginView.as_view(), name='login'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)