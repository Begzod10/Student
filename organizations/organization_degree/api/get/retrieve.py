from rest_framework import generics

from organizations.models.models import OrganizationDegrees
from organizations.organization_degree.serializers.get.retrieve_view import OrganizationDegreesRetrieveSerializer


class OrganizationDegreesRetrieve(generics.RetrieveAPIView):
    queryset = OrganizationDegrees.objects.all()
    serializer_class = OrganizationDegreesRetrieveSerializer
