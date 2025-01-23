from django.urls import path

from organizations.organization_user.api.crud.create import OrganizationUserCreateView
from organizations.organization_user.api.crud.update import OrganizationUserUpdateView
from organizations.organization_user.api.crud.destroy import OrganizationUserDestroyApiView
from organizations.organization_gallery.api.crud.update import OrganizationGalleryUpdateView
urlpatterns = [
    path('create/', OrganizationUserCreateView.as_view(), name='create'),
    path('update/<pk>/', OrganizationUserUpdateView.as_view(), name='update'),
    path('update-file/<pk>/', OrganizationGalleryUpdateView.as_view(), name='update-file'),
    path('delete/<pk>/', OrganizationUserDestroyApiView.as_view(), name='delete'),
]
