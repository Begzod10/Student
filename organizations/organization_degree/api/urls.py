from django.urls import path, include

urlpatterns = [
    path('organization-degree/crud/',include('organizations.organization_degree.api.crud.urls')),
    path('organization-degree/get/', include('organizations.organization_degree.api.get.urls')),

]
