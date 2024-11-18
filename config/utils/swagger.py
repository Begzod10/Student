from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Sen talaba",
        default_version='v1',
        description="API documentation for your application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@sentalaba.com"),
        license=openapi.License(name="SSL License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
