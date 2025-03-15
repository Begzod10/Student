from rest_framework import generics

from organizations.models import OrganizationType
from organizations.organization_type.serializers.get.retrieve_view import OrganizationTypeSerializer


class RetrieveOrganizationTypeInfos(generics.RetrieveAPIView):
    queryset = OrganizationType.objects.all()
    serializer_class = OrganizationTypeSerializer
