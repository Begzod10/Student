from django.urls import path, include

urlpatterns = [
    path('get/', include('organizations.organization_landing_page.api.get.urls')),
    path('crud/', include('organizations.organization_landing_page.api.crud.urls')),
]
