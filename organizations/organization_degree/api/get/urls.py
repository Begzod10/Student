from django.urls import path

from organizations.organization_degree.api.get.retrieve import OrganizationDegreesRetrieve

urlpatterns = [
    path('<int:pk>/', OrganizationDegreesRetrieve.as_view(), name='user-retrieve'),
]