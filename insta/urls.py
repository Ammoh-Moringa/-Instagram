from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns=[
    url(r'^$',views.home, name='home'),
    url('register/',views.signup, name='signup'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)