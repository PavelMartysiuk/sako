from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from sako import settings


schema_view = get_schema_view(
   openapi.Info(
      title='Innowise automation snippets API',
      default_version='v1',
      description='API description',
      contact=openapi.Contact(email='company@sako.com'),
      license=openapi.License(name='Sako License'),
   ),
   url=settings.SWAGGER_LINK,
   public=True,
   permission_classes=(permissions.AllowAny,),
)