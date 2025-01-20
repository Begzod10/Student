from django.urls import path
from organizations.organization.api.get.retrieve_view import RetrieveOrganizationInfos
from organizations.organization.api.get.filter_for_type import FilterForTypeOrganizationView
from django.urls import path, include

urlpatterns = [

    path('<int:pk>/', RetrieveOrganizationInfos.as_view(), name='user-retrieve'),
    path('filter_for_type/', FilterForTypeOrganizationView.as_view(), name='filter_for_type'),
]
