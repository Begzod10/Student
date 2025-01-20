from rest_framework import generics

from organizations.models.organization_landing_page import OrganizationAdvantage
from organizations.organization_advantage.serializers.get.retrieve_view import OrganizationAdvantageSerializer


class OrganizationAdvantageList(generics.ListAPIView):
    queryset = OrganizationAdvantage.objects.all()
    serializer_class = OrganizationAdvantageSerializer

    def get_queryset(self):
        organization_id = self.request.query_params.get('organization_id', None)
        if organization_id is not None:
            return OrganizationAdvantage.objects.filter(organization_id=organization_id)
        return None
