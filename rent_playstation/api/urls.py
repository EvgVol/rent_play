from django.urls import include, path
from rest_framework import routers

from .views import (SignUp, UsersViewSet, get_token)


router_v1 = routers.DefaultRouter()
router_v1.register(r'users', UsersViewSet, basename='users')

jwt_patterns = [
    path('token/', get_token, name='get_token'),
    path('signup/', SignUp.as_view(), name='signup'),
]

urlpatterns = [
    path('v1/auth/', include(jwt_patterns)),
    path('v1/', include(router_v1.urls)),
]
