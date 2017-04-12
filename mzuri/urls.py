"""mzuri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mzuriapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^artist/sign-in/$', auth_views.login,
    {'template_name': 'artist/sign_in.html'},
    name = 'artist-sign-in'),
    url(r'^artist/sign-out/$', auth_views.logout,
    {'next_page': '/'},
    name = 'artist-sign-out'),
    url(r'^artist/sign-up/$', views.artist_sign_up,
    name = 'artist-sign-up'),
    url(r'^artist/$', views.artist_home, name='artist-home')

] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
