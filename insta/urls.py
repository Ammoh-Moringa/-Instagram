from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^$',views.signup, name='signup'),
    url(r'^$',views.search, name='search'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^upload/$', views.upload_image, name='upload_image'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)