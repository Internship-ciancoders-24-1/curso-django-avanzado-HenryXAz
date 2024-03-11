"""Circle views"""

# Django rest framework
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

# models
from cride.circles.models import Circle, MemberShip

# serializers
from cride.circles.serializers import CircleModelSerializer

# permissions
from cride.circles.permissions import IsCircleAdmin


class CircleViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Circle view set"""
    # queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer
    lookup_field = 'slug_name'
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Restrict list to public-only circles"""
        queryset = Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset

    def get_permissions(self):
        """Asign permissions based on action"""
        permissions = [IsAuthenticated]
        if self.action in ['update', 'partial_update']:
            permissions.append(IsCircleAdmin)
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        """Assign circle admin"""
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        MemberShip.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitations=10,
        )
