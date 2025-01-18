from django.urls import path

from organizations.organization_gallery.api.crud.create import OrganizationGalleryCreateView,OrganizationGalleryFileCreateView
from organizations.organization_gallery.api.crud.update import OrganizationGalleryUpdateView
from organizations.organization_gallery.api.crud.destroy import OrganizationGalleryDestroyApiView

urlpatterns = [
    path('create/', OrganizationGalleryCreateView.as_view(), name='create'),
    path('create-file/', OrganizationGalleryFileCreateView.as_view(), name='create-file/'),
    path('update/<pk>/', OrganizationGalleryUpdateView.as_view(), name='update'),
    path('delete/<pk>/', OrganizationGalleryDestroyApiView.as_view(), name='delete'),
]
