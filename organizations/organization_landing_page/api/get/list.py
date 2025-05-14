from rest_framework import generics

from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization_landing_page.serializers.get.retrieve_view import OrganizationLandingPageSerializer
from rest_framework import generics
from rest_framework.response import Response


class OrganizationLandingPageList(generics.ListAPIView):
    queryset = OrganizationLandingPage.objects.filter(deleted=False).order_by('id').all()
    serializer_class = OrganizationLandingPageSerializer

    def get_queryset(self):
        organization_id = self.request.query_params.get('organization_id', None)
        year_id = self.request.query_params.get('year_id', None)
        degree_id = self.request.query_params.get('degree_id', None)

        return OrganizationLandingPage.objects.filter(organization_id=organization_id, year_id=year_id,
                                                      degree_id=degree_id, deleted=False)
