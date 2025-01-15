from django.urls import path

from organizations.organization_advantage.api.get.list import OrganizationAdvantageList
from organizations.organization_advantage.api.get.retrieve import OrganizationAdvantageRetrieve

urlpatterns = [
    path('<int:pk>/', OrganizationAdvantageRetrieve.as_view(), name='organization-gallery'),
    path('', OrganizationAdvantageList.as_view(), name='organization-gallery-list'),
]
