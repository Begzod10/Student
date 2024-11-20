from django.urls import path

from organizations.organization_landing_page.api.crud.create import OrganizationLandingPageCreateView

urlpatterns = [
    path('create/', OrganizationLandingPageCreateView.as_view(), name='create'),
]
