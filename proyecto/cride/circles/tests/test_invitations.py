"""Invitations test"""

# django
from django.test import TestCase

# rest framework
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token


# model
from cride.circles.models import Circle, MemberShip, Invitation
from cride.users.models import User, Profile


class MemberInvitationApiTestCase(APITestCase):
    """Member invitation test case"""

    def setUp(self):
        """Test case setup"""
        self.user = User.objects.create(
            first_name='Henry',
            last_name='Xitimul',
            email='henry@example.com',
            username='henrygus',
            password='admin12345'
        )

        self.profile = Profile.objects.create(
            user=self.user
        )

        self.circle = Circle.objects.create(
            name='Facultad de ingenieria',
            slug_name='ing_facultad',
            about='Grupo oficial de ingeniería',
            verified=True
        )
        self.membership = MemberShip.objects.create(
            user=self.user,
            profile=self.profile,
            circle=self.circle,
            remaining_invitations=10
        )

        # Auth
        self.token = Token.objects.create(user=self.user).key
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))

        # URL
        self.url = '/circles/{}/members/{}/invitations/'.format(
            self.circle.slug_name,
            self.user.username
        )

    def test_response_success(self):
        """Verify request success"""
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_invitation_creation(self):
        """Verify invitation are generated if none exists previously"""
    # Invitations in DB must be 0
        self.assertEqual(Invitation.objects.count(), 0)

        # Call member invitations url
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        # Verify new invitations were created
        invitations = Invitation.objects.filter(issued_by=self.user)
        self.assertEqual(invitations.count(), self.membership.remaining_invitations)

        for invitation in invitations:
            self.assertIn(invitation.code, request.data['invitations'])



