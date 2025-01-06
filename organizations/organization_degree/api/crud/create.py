from rest_framework.generics import CreateAPIView

from organizations.models import OrganizationDegrees
from organizations.organization_degree.serializers.crud.crud import OrganizationDegreesCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticated


class OrganizationDegreesCreateView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = OrganizationDegrees.objects.all()
    serializer_class = OrganizationDegreesCreateUpdateSerializer
