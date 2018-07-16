"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path, include

from profiles import views as profiles_views
from contact import views as contact_views
from checkout import views as checkout_views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', profiles_views.home, name='home'),
    re_path(r'^about/$', profiles_views.about, name='about'),
    re_path(r'^profile/$', profiles_views.userProfile, name='profile'),
    re_path(r'^checkout/$', checkout_views.checkout, name='checkout'),
    re_path(r'^contact/$', contact_views.contact, name='contact'),
    re_path(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)