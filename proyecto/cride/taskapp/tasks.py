"""Celery tasks"""

# django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from django.conf import settings

# celery
from celery import shared_task, current_task

# utilities
import jwt
from datetime import timedelta


# models
from cride.users.models import User
from cride.rides.models import Ride


@shared_task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk):
    """Send account verification link to given user"""
    user = User.objects.get(
        pk=user_pk
    )
    verification_token = generate_verification_token(user)
    subject = 'welcome @{}! Verify your account to start using Comparte Ride '.format(user.username)
    from_email = 'Comparte Ride <noreply@comparteride.com>'
    content = render_to_string(
        'emails/users/account_verification.html',
        {'token': verification_token, 'user': user}
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()


def generate_verification_token(user):
    """"generate verification token"""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        'user': user.username,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation',
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return token


@shared_task(name='disable_finished_rides', run_every=timedelta(seconds=3))
def disable_finished_rides():
    """Disable finished rides"""
    now = timezone.now()
    offset = now + timedelta(seconds=5)

    #  update rides that have already finished
    rides = Ride.objects.filter(arrival_date_gte=now,
                                arrival_date_lte=offset,
                                is_active=True)
    rides.update(is_active=False)

