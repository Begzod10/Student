from django.urls import path

from organizations.organization_degree.api.get.list import OrganizationDegreesList,OrganizationDegreesListByOrganizationType
from organizations.organization_degree.api.get.retrieve import OrganizationDegreesRetrieve

urlpatterns = [
    path('<int:pk>/', OrganizationDegreesRetrieve.as_view(), name='user-retrieve'),
    path('', OrganizationDegreesList.as_view(), name='user-list'),
    path('list/<int:pk>/', OrganizationDegreesListByOrganizationType.as_view(), name='user-list'),
]
