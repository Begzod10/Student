from django.urls import path

from organizations.organization_degree.api.crud.create import OrganizationDegreesCreateView
from organizations.organization_degree.api.crud.update import OrganizationDegreesUpdateView
from organizations.organization_degree.api.crud.delete import OrganizationDegreesDeleteView

urlpatterns = [
    path('create/', OrganizationDegreesCreateView.as_view(), name='create'),
    path('update/<pk>/', OrganizationDegreesUpdateView.as_view(), name='update'),
    path('delete/<pk>/', OrganizationDegreesDeleteView.as_view(), name='delete'),
]
