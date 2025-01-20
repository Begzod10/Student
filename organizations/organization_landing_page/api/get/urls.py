from django.urls import path

from organizations.organization_landing_page.api.get.list import OrganizationLandingPageList
from organizations.organization_landing_page.api.get.retrieve import OrganizationLandingPageRetrieve

urlpatterns = [
    path('<int:pk>/', OrganizationLandingPageRetrieve.as_view(), name='organization-gallery'),
    path('', OrganizationLandingPageList.as_view(), name='organization-gallery-list'),
]
