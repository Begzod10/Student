from rest_framework import generics

from organizations.models.models import OrganizationGallery
from organizations.organization_gallery.serializers.get.retrieve_view import OrganizationGallerySerializer


class OrganizationGalleryRetrieve(generics.RetrieveAPIView):
    queryset = OrganizationGallery.objects.all()
    serializer_class = OrganizationGallerySerializer
