from django.conf.urls import patterns, include, url
from django.contrib import admin
from establishmentDataManagement.admin import admin_site

urlpatterns = patterns(
    '',
    (r'^accounts/', include('allauth.urls')),
    (r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    (r'^admin/', include(admin.site.urls)),
    (r'^adminC/', include(admin_site.urls)),
)
