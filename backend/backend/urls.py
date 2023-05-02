from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi, views
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static


schema_view = views.get_schema_view(
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
    path('', include('core.urls'), name='index')
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )