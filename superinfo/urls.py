"""superinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
# import for Serving files uploaded by a user during development
from django.conf import settings
from django.conf.urls.static import static, serve


urlpatterns = [
    path('commingsoon/', include('comingsoon.urls')),
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
]

# serving for Debug=false in development
if settings.DEBUG is False:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve,
                {'document_root': settings.STATIC_ROOT}),
    ]

'''
Text for admin section
'''
# admin titles
admin.site.site_header = "SuperInfo Adminstration"
# admin.site.site_url = None
admin.site.site_title = "SuperInfo Adminstration"
