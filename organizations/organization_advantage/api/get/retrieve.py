from rest_framework import generics

from organizations.models.organization_landing_page import OrganizationAdvantage
from organizations.organization_advantage.serializers.get.retrieve_view import OrganizationAdvantageSerializer


class OrganizationAdvantageRetrieve(generics.RetrieveAPIView):
    queryset = OrganizationAdvantage.objects.all()
    serializer_class = OrganizationAdvantageSerializer
