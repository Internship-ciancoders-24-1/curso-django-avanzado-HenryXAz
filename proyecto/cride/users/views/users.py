"""Users views"""

from rest_framework import status
from rest_framework.response import Response
# Django rest framework
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action

# serializers
from cride.users.serializers import (
    UserLoginSerializer,
    UserSignUpSerializer,
    UserModelSerializer,
    AccountVerificationSerializer,
)


class UserViewSet(viewsets.GenericViewSet):
    """User view set
    Handle signup, login and account verification
    """

    @action(detail=False, methods=['POST'])
    def signup(self, request):
        """User signup endpoint"""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        data = UserModelSerializer(user).data

        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def login(self, request):
        """User login endpoint"""

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()

        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }

        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def verify(self, request):
        """Handle http POST request"""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            'msg': 'Congratulations, now go share some rides!',
        }
        return Response(data=data, status=status.HTTP_200_OK)


# class UserLoginAPIView(APIView):
#     """User Login APIView"""
#
#     def post(self, request, *args, **kwargs):
#         """Handle http request"""
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user, token = serializer.save()
#
#         data = {
#             'user': UserModelSerializer(user).data,
#             'access_token': token
#         }
#
#         return Response(data=data, status=status.HTTP_201_CREATED)
#
#
# class UserSignUpAPIView(APIView):
#     """User sign up APIView"""
#
#     def post(self, request, *args, **kwargs):
#         """Handle http POST request"""
#         serializer = UserSignUpSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#
#         data = UserModelSerializer(user).data
#
#         return Response(data=data, status=status.HTTP_201_CREATED)
#
#
# class AccountVerificationAPIView(APIView):
#     """Account verification APIView"""
#
#     def post(self, request, *args, **kwargs):
#         """Handle http POST request"""
#         serializer = AccountVerificationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         data = {
#             'msg': 'Congratulations, now go share some rides!',
#         }
#         return Response(data=data, status=status.HTTP_200_OK)
