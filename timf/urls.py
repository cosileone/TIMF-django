"""Project URL Configuration

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
from django.urls import include, path, re_path
from django.contrib import admin

from . import views

urlpatterns = [
    # apps
    path('test/', views.test, name='test'),
    path('items/', include('items.urls')),
    path('admin/', admin.site.urls),

    # api
    path('', include('timf.api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # vue
    path('', views.vue),

    # SPA catch-all
    re_path('.*', views.vue, name='catchall'),
    # re_path('.*[^.]+$', views.vue, name='catchall'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG and settings.DJANGO_TOOLBAR:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
