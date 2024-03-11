"""Users URLs"""
# Django
from django.urls import path, include

# rest framework
from rest_framework.routers import DefaultRouter


# views
from cride.users.views import users as users_views
# from cride.users.views import (
#     UserLoginAPIView,
#     UserSignUpAPIView,
#     AccountVerificationAPIView,
# )

router = DefaultRouter()
router.register(r'users', users_views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]



# router = DefaultRouter()
# router.register(r'users', users_views.UserViewSet, basename='user')

# url pattenrs
# urlpatterns = [
#     path('', include(router.urls))
    # path('users/login', UserLoginAPIView.as_view(), name='login'),
    # path('users/signup', UserSignUpAPIView.as_view(), name='signup'),
    # path('users/verify', AccountVerificationAPIView.as_view(), name='verify')
# ]

