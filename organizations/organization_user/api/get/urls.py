from django.urls import path

from organizations.organization_user.api.get.list import OrganizationUserListView
from organizations.organization_user.api.get.retrieve import OrganizationUserDetailView

urlpatterns = [
    path('<int:organization_id>/', OrganizationUserListView.as_view(),
         name='organization-user-list'),
    path('', OrganizationUserListView.as_view(), name='organization-user-list'),
]
