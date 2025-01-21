from django.urls import path
from organizations.organization.api.get.retrieve_view import RetrieveOrganizationInfos
from organizations.organization.api.get.filter_for_type import FilterForTypeOrganizationView
from django.urls import path, include
from organizations.organization.views.filters import organizations_filter,organizations_get_filtereds

urlpatterns = [
    path('<int:pk>/', RetrieveOrganizationInfos.as_view(), name='user-retrieve'),
    path('organizations_filter/<int:pk>/', organizations_filter, name='organizations-filter'),
    path('organizations_get_filtereds/', organizations_get_filtereds, name='organizations-filter'),
    path('filter_for_type/', FilterForTypeOrganizationView.as_view(), name='filter_for_type'),
]
