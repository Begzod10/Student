from django.urls import path, include

urlpatterns = [
    path('get/', include('organizations.organization_advantage.api.get.urls')),
    path('crud/', include('organizations.organization_advantage.api.crud.urls')),
]
