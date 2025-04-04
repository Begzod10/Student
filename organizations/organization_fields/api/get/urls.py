from django.urls import path

from .list_from_organization_type import OrganizationFieldsListView,OrganizationFields2ListView

urlpatterns = [

    path('organization-fields/<int:pk>/', OrganizationFieldsListView.as_view(), name='organization-fields-list'),
    path('organization-fields2/<int:pk>/', OrganizationFields2ListView.as_view(), name='organization-fields-list'),
]
