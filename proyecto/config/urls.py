"""Main URLs module."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    # Main Urls
    path('', include(('cride.users.urls', 'users'), namespace='users')),
    path('', include(('cride.circles.urls', 'circles'), namespace='circles')),
    path('', include(('cride.rides.urls', 'rides'), namespace='rides')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
