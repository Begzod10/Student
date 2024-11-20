from django.urls import path

from organizations.organization.api.crud.create import OrganizationCreateApiView
from organizations.organization.api.crud.update import OrganizationUpdateApiView
from organizations.organization.api.crud.destroy import OrganizationTypeDestroyApiView

urlpatterns = [
    path('create/', OrganizationCreateApiView.as_view(), name='create'),
    path('update/<pk>/', OrganizationUpdateApiView.as_view(), name='update'),
    path('delete/<pk>/', OrganizationTypeDestroyApiView.as_view(), name='delete'),
]
