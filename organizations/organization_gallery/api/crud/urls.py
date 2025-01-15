from django.urls import path

from organizations.organization_gallery.api.crud.create import OrganizationGalleryCreateView
from organizations.organization_gallery.api.crud.update import OrganizationGalleryUpdateView
from organizations.organization_gallery.api.crud.destroy import OrganizationGalleryDestroyApiView

urlpatterns = [
    path('create/', OrganizationGalleryCreateView.as_view(), name='create'),
    path('update/<pk>/', OrganizationGalleryUpdateView.as_view(), name='update'),
    path('delete/<pk>/', OrganizationGalleryDestroyApiView.as_view(), name='delete'),
]
