from rest_framework import generics

from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization_landing_page.serializers.get.retrieve_view import OrganizationLandingPageSerializer


class OrganizationLandingPageRetrieve(generics.RetrieveAPIView):
    queryset = OrganizationLandingPage.objects.all()
    serializer_class = OrganizationLandingPageSerializer

    def get_queryset(self):
        organization_id = self.request.query_params.get('organization_id', None)
        print(f"Organization ID: {organization_id}")
        if organization_id is not None:
            queryset = OrganizationLandingPage.objects.filter(organization_id=organization_id)
            print(f"Queryset: {queryset}")
            return queryset
        return OrganizationLandingPage.objects.none()