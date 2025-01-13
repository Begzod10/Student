from rest_framework.generics import UpdateAPIView
from organizations.organization_degree.serializers.crud.crud import OrganizationDegreesCreateUpdateSerializer
from organizations.models.models import OrganizationDegrees
from rest_framework.permissions import IsAuthenticated


class OrganizationDegreesUpdateView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = OrganizationDegrees.objects.all()
    serializer_class = OrganizationDegreesCreateUpdateSerializer
