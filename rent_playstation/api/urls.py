from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenVerifyView,
                                            TokenRefreshView)

from .views import ConsoleViewSet, OrderViewSet

v1_router = routers.DefaultRouter()
v1_router.register(r'consoles', ConsoleViewSet, basename='consoles')
# v1_router.register(
#     r'rental-rate',
#     RentalRateViewSet,
#     basename='rental_rate'
# )
v1_router.register(r'orders', OrderViewSet, basename='orders')

jwt_patterns = [
    path(
        'create/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path(
        'verify/',
        TokenVerifyView.as_view(),
        name='token_verify'),
]

urlpatterns = [
    path('v1/jwt/', include(jwt_patterns)),
    path('v1/', include(v1_router.urls)),
]
