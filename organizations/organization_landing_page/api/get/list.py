from rest_framework import generics

from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization_landing_page.serializers.get.retrieve_view import OrganizationLandingPageSerializer


class OrganizationLandingPageList(generics.ListAPIView):
    queryset = OrganizationLandingPage.objects.all()
    serializer_class = OrganizationLandingPageSerializer

    def get_queryset(self):
        organization_id = self.request.query_params.get('organization_id', None)
        if organization_id is not None:
            return OrganizationLandingPage.objects.filter(organization_id=organization_id)
        return None

