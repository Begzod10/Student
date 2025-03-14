from django.urls import path, include

urlpatterns = [
    path('organization/get/', include('organizations.organization.api.get.urls')),
    path('organization/crud/', include('organizations.organization.api.crud.urls')),
    path('organization/filter/', include('organizations.organization.api.crud.urls')),
    path('organization_type/get/', include('organizations.organization_type.api.get.urls')),
    path('organization_type/crud/', include('organizations.organization_type.api.crud.urls')),
    path('organization_landing_page/', include('organizations.organization_landing_page.api.urls')),
    path('organization_degree/', include('organizations.organization_degree.api.crud.urls')),
    path('organization_advantage/', include('organizations.organization_advantage.api.urls')),
    path('organization_gallery/crud/', include('organizations.organization_gallery.api.crud.urls')),
    path('organization_gallery/get/', include('organizations.organization_gallery.api.get.urls')),
    path('organization_user/crud/', include('organizations.organization_user.api.crud.urls')),
    path('organization_user/get/', include('organizations.organization_user.api.get.urls')),
    path('organization_fields/', include('organizations.organization_fields.urls')),
    path('', include('organizations.news.urls')),
]
