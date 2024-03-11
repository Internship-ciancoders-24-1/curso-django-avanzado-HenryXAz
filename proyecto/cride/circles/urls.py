"""Circles URL"""

# django
from django.urls import path, include

# rest framework
from rest_framework.routers import DefaultRouter

# views
from cride.circles.views import circles as circle_views

router = DefaultRouter()
router.register(r'circles', circle_views.CircleViewSet, basename='circle')

urlpatterns = [
    path('', include(router.urls)),
]
