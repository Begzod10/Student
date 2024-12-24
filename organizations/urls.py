from django.urls import path
from organizations.views import StudentRequestListView, StudentRequestRetrieveView, student_request_dashboard
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('organization/get/', include('organizations.organization.api.get.urls')),
    path('organization/crud/', include('organizations.organization.api.crud.urls')),
    path('organization_type/get/', include('organizations.organization_type.api.get.urls')),
    path('organization_landing_page/', include('organizations.organization_landing_page.api.crud.urls')),
    path('organization_degree/', include('organizations.organization_degree.api.crud.urls')),
]
