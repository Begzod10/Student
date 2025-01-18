from django.urls import path

from .list_from_organization_type import OrganizationFieldsListView

urlpatterns = [

    path('organization-fields/<int:pk>/', OrganizationFieldsListView.as_view(), name='organization-fields-list'),
]
