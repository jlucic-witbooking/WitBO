import allauth
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from allauth.account.views import login
from establishmentDataManagement.admin import admin_site

urlpatterns = patterns(
    '',
    (r'^accounts/', include('allauth.urls')),
    (r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    (r'^admin/login/', allauth.account.views.login), # redirect admin Login to base login
    (r'^admin/', include(admin.site.urls)),
    (r'^adminC/', include(admin_site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
