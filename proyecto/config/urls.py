"""Main URLs module."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    # Main Urls
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
