from rest_framework import generics

from organizations.models.models import OrganizationGallery
from organizations.organization.serializers.get.retrieve_view import OrganizationGallerySerializer


class OrganizationGalleryList(generics.ListAPIView):
    serializer_class = OrganizationGallerySerializer

    def get_queryset(self):
        organization_id = self.request.query_params.get('organization_id', None)
        if organization_id is not None:
            return OrganizationGallery.objects.filter(organization_id=organization_id)
        return OrganizationGallery.objects.none()  # Or handle differently if you want to return all
