from rest_framework import generics

from organizations.models.organization_landing_page import OrganizationAdvantage
from organizations.organization_advantage.serializers.crud.crud import OrganizationAdvantageCreateUpdateSerializer


class OrganizationAdvantageDestroyApiView(generics.DestroyAPIView):
    queryset = OrganizationAdvantage.objects.all()
    serializer_class = OrganizationAdvantageCreateUpdateSerializer
