from rest_framework import generics

from organizations.models.models import OrganizationGallery
from organizations.organization_gallery.serializers.get.retrieve_view import OrganizationGallerySerializer


class OrganizationGalleryList(generics.ListAPIView):
    queryset = OrganizationGallery.objects.all()
    serializer_class = OrganizationGallerySerializer

    def get_queryset(self):
        organization_id = self.request.query_params.get('organization_id', None)
        if organization_id is not None:
            return OrganizationGallery.objects.filter(organization_id=organization_id)
        return None
