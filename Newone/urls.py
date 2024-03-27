"""
URL configuration for Newone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from FirstDjangoAuth.views import *


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name="hai"),

    path('submit/', login_process, name="submit"),
    path('sign_invite/', sign_invite, name="sign_invite"),
    path('submit_2/', login_process_2, name="submit_2"),
    path('dash/', dash, name="dash"),
    path('logout_page/', logout_page, name="logout_page"),

    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)