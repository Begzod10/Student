from django.urls import path

from organizations.organization_gallery.api.get.list import OrganizationGalleryList
from organizations.organization_gallery.api.get.retrieve import OrganizationGalleryRetrieve

urlpatterns = [
    path('', OrganizationGalleryRetrieve.as_view(), name='organization-gallery'),
    path('list', OrganizationGalleryList.as_view(), name='organization-gallery-list'),
]
