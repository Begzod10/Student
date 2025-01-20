from rest_framework.generics import CreateAPIView

from organizations.models.organization_landing_page import OrganizationAdvantage
from organizations.organization_advantage.serializers.crud.crud import OrganizationAdvantageCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticated


class OrganizationAdvantageCreateView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = OrganizationAdvantage.objects.all()
    serializer_class = OrganizationAdvantageCreateUpdateSerializer
