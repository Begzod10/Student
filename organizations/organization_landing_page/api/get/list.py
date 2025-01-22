from rest_framework import generics

from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization_landing_page.serializers.get.retrieve_view import OrganizationLandingPageSerializer
from rest_framework import generics
from rest_framework.response import Response


class OrganizationLandingPageList(generics.ListAPIView):
    queryset = OrganizationLandingPage.objects.all()
    serializer_class = OrganizationLandingPageSerializer

    def get_queryset(self):
        organization_id = self.request.query_params.get('organization_id', None)
        if organization_id is not None:
            return OrganizationLandingPage.objects.filter(organization_id=organization_id)
        return None

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        grant_true_records = queryset.filter(grant=True)
        grant_false_records = queryset.filter(grant=False)
        grant_true_serializer = OrganizationLandingPageSerializer(grant_true_records, many=True)
        grant_false_serializer = OrganizationLandingPageSerializer(grant_false_records, many=True)
        return Response({
            'grant_true': grant_true_serializer.data,
            'grant_false': grant_false_serializer.data
        })

