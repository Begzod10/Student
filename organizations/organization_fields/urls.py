from django.urls import path,include

urlpatterns = [
    path('get/', include('organizations.organization_fields.api.get.urls')),
    path('crud/', include('organizations.organization_fields.api.crud.urls')),
]
