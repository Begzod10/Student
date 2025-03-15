from rest_framework.generics import UpdateAPIView
from organizations.models.organization_landing_page import OrganizationAdvantage
from organizations.organization_advantage.serializers.crud.crud import OrganizationAdvantageCreateUpdateSerializer


class OrganizationAdvantageUpdateView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = OrganizationAdvantage.objects.all()
    serializer_class = OrganizationAdvantageCreateUpdateSerializer


