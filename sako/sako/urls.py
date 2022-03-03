
from django.contrib import admin
from django.urls import path, re_path, include

from sako import settings

from core.swagger.swagger import schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.api.v1.urls')),
]

if settings.DEBUG:
    urlpatterns.extend((
        re_path(r'api/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path(r'api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path(r'api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ))