"""Circles admin"""

# django
from django.contrib import admin

# utils
from cride.utils.models import CRideModels

# model

from cride.circles.models import Circle


@admin.register(Circle)
class Circle(admin.ModelAdmin):
    """Circle admin"""
    list_display = ('slug_name', 'is_public', 'name', 'verified', 'is_limited', 'members_limit',)
    search_fields = ('slug_name', 'name',)
    list_filter = ('is_public', 'verified', 'is_limited')


