from rest_framework import generics

from organizations.models.models import OrganizationType
from organizations.organization_type.serializers.crud.create import OrganizationTypeCreateSerializer


class CreateOrganizationTypeView(generics.CreateAPIView):
    queryset = OrganizationType.objects.all()
    serializer_class = OrganizationTypeCreateSerializer
