from django.urls import path

from organizations.organization_landing_page.api.crud.create import OrganizationLandingPageCreateView
from organizations.organization_landing_page.api.crud.update import OrganizationLandingPageUpdateView
from organizations.organization_landing_page.api.crud.destroy import OrganizationLandingPageDestroyApiView

urlpatterns = [
    path('create/', OrganizationLandingPageCreateView.as_view(), name='create'),
    path('update/<pk>/', OrganizationLandingPageUpdateView.as_view(), name='update'),
    path('delete/<pk>/', OrganizationLandingPageDestroyApiView.as_view(), name='update'),
]
