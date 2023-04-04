from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include


schema_view = get_schema_view(
   openapi.Info(
      title="RentPlay API",
      default_version='v1',
      description="Документация для приложения backend проекта Rent&Play",
      contact=openapi.Contact(email="admin@rentplay"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls',)),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), 
       name='schema-redoc'),
]
