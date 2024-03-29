"""Users serializers"""
# django
from django.conf import settings
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

# Django rest framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# models
from cride.users.models import (
    User,
    Profile
)


# tasks
from cride.taskapp.tasks import send_confirmation_email

# utilities
import jwt
from datetime import timedelta

class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        """Meta class"""

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
        )


class UserSignUpSerializer(serializers.Serializer):
    """User signup serializer
    handle sing up data validation and user/profile creation
    """
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ])

    #  Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed"
    )
    phone_number = serializers.CharField(validators=[phone_regex], max_length=17)

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        """Verify password match"""
        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:
            raise serializers.ValidationError('Passwords does not match')

        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation"""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False)
        Profile.objects.create(user=user)
        # self.send_confirmation_email(user)
        send_confirmation_email.delay(user_pk=user.pk)
        return user

    # def send_confirmation_email(self, user):
    #     """Send account verification link to given user"""
    #     verification_token = self.generate_verification_token(user)
    #     subject = 'welcome @{}! Verify your account to start using Comparte Ride '.format(user.username)
    #     from_email = 'Comparte Ride <noreply@comparteride.com>'
    #     content = render_to_string(
    #         'emails/users/account_verification.html',
    #         {'token': verification_token, 'user': user}
    #     )
    #     msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    #     msg.attach_alternative(content, "text/html")
    #     msg.send()
    #
    # def generate_verification_token(self, user):
    #     """"generate verification token"""
    #     exp_date = timezone.now() + timedelta(days=3)
    #     payload = {
    #         'user': user.username,
    #         'exp': int(exp_date.timestamp()),
    #         'type': 'email_confirmation',
    #     }
    #     token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    #
    #     return token


class UserLoginSerializer(serializers.Serializer):
    """User Login Serializer
    Handle the login request data
    """
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials"""
        user = authenticate(username=data['email'], password=data['password'])

        if not user:
            raise serializers.ValidationError('invalid credentials')

        if not user.is_verified:
            raise serializers.ValidationError('Account is not active yet :(')

        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token"""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class AccountVerificationSerializer(serializers.Serializer):
    """Account verification serializer"""
    token = serializers.CharField()

    def validate(self, data):
        """Verify token is valid"""
        try:
            token_str = data.get('token')
            token = token_str.encode()
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired')
        except jwt.PyJWTError as e:
            print('el error', e)
            raise serializers.ValidationError('Invalid token')

        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Invalid token')

        self.context['payload'] = payload
        return data

    def save(self):
        """Update users verify status"""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])

        user.is_verified = True
        user.save()
