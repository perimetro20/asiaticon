"""asiaticon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/

"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('', include('base.urls')),
    url('', include('social_django.urls', namespace='social')),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^importing/', include('importing.urls')),
    url(r'^tosp_auth/', include('tosp_auth.urls')),
    url(r'^user_profiles/', include('user_profiles.urls'))
]
