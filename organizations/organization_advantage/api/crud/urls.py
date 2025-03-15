from django.urls import path

from organizations.organization_advantage.api.crud.create import OrganizationAdvantageCreateView
from organizations.organization_advantage.api.crud.update import OrganizationAdvantageUpdateView
from organizations.organization_advantage.api.crud.destroy import OrganizationAdvantageDestroyApiView

urlpatterns = [
    path('create/', OrganizationAdvantageCreateView.as_view(), name='create'),
    path('update/<pk>/', OrganizationAdvantageUpdateView.as_view(), name='update'),
    path('delete/<pk>/', OrganizationAdvantageDestroyApiView.as_view(), name='delete'),
]
