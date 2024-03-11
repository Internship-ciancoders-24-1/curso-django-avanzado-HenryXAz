"""Circles URL"""

# django
from django.urls import path, include

# rest framework
from rest_framework.routers import DefaultRouter

# views
from cride.circles.views import circles as circle_views
from cride.circles.views.memberships import MembershipViewSet

router = DefaultRouter()
# router.register(r'circles', circle_views.CircleViewSet, basename='circle')
router.register(
  r'circles/(?P<slug_name>[-a-zA-Z0-0_]+)/members',
  MembershipViewSet,
  basename='membership'
)

urlpatterns = [
    path('', include(router.urls)),
]
