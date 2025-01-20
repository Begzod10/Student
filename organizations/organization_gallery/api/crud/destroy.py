from rest_framework import generics

from organizations.models import OrganizationGallery
from organizations.organization_gallery.serializers.crud.crud import OrganizationGalleryCreateUpdateSerializer


class OrganizationGalleryDestroyApiView(generics.DestroyAPIView):
    queryset = OrganizationGallery.objects.all()
    serializer_class = OrganizationGalleryCreateUpdateSerializer
