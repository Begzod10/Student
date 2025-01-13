from django.urls import path

from organizations.organization_degree.api.crud.create import OrganizationDegreesCreateView
from organizations.organization_degree.api.crud.update import OrganizationDegreesUpdateView

urlpatterns = [
    path('create/', OrganizationDegreesCreateView.as_view(), name='create'),
    path('update/<pk>/', OrganizationDegreesUpdateView.as_view(), name='update'),
    # path('delete/<pk>/', OrganizationDegreeDeleteView.as_view(), name='delete'),
]
