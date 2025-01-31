from django.urls import path

from organizations.organization_type.api.get.list import OrganizationTypeListView
from organizations.organization_type.api.get.retrieve_view import RetrieveOrganizationTypeInfos

urlpatterns = [
    path('<pk>', RetrieveOrganizationTypeInfos.as_view()),
    path('list/', OrganizationTypeListView.as_view())
]
