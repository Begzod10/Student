from rest_framework import generics

from organizations.models.models import OrganizationType
from organizations.organization_type.serializers.crud.create import OrganizationTypeCreateSerializer


class UpdateOrganizationTypeView(generics.UpdateAPIView):
    queryset = OrganizationType.objects.all()
    serializer_class = OrganizationTypeCreateSerializer
