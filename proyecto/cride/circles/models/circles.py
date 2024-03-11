
# Django
from django.db import models

# utils
from cride.utils.models import CRideModels


class Circle(CRideModels):
    """Circle model"""

    name = models.CharField("circle name", max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle descriptio', max_length=255)
    picture = models.ImageField(upload_to='circles/pages', blank=True, null=True)

    members = models.ManyToManyField(
        'users.User',
        through='circles.MemberShip',
        through_fields=('circle', 'user'),
    )

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circles',
        default=False,
        help_text='Verified circles are also known as official communities'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Public circles are listed in the main page so everyone known about their existence'
    )

    is_limited = models.BooleanField(
        'limited circles',
        default=True,
        help_text='limited circles can grow up to a fixed number of members'
    )

    members_limit = models.PositiveIntegerField(
        'members limit',
        default=0,
        help_text='if circle is limited, this will be the limit on the number of members'
    )

    def __str__(self):
        """Return circle name"""
        return self.name

    class Meta(CRideModels.Meta):
        ordering = ['-rides_taken', '-rides_offered']



