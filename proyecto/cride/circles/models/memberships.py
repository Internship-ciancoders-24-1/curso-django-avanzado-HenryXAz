"""Membership model"""

# Django
from django.db import models

# utilities
from utils.models import CRideModels


class MemberShip(CRideModels):
    """Membership model
    membership is the table that holds the relationship between the user and the circle
    """

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    circle = models.ForeignKey('circles.Circle', on_delete=models.CASCADE)

    is_admin = models.BooleanField(
        'circle admin',
        default=False,
        help_text='Circle admins can update the circles data and manage its members',
        )

    # invitations
    used_invitations = models.PositiveIntegerField(default=0)
    remaining_invitations = models.PositiveIntegerField(default=0)
    invited_by = models.ForeignKey(
        'users.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='invited_by'
    )

    # stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)

    # Status
    is_active = models.BooleanField(
        'active status',
        default=True,
        help_text='Only active users are allowed to interact in the circle',
    )

    def __str__(self):
        """Return username and circle"""
        return '@{} at #{}'.format(
            self.user.username,
            self.circle.slug_name)

