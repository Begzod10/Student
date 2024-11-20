from rest_framework import generics

from organizations.models import Organization
from organizations.organization_type.serializers.get.retrieve_view import OrganizationTypeSerializer


class OrganizationTypeDestroyApiView(generics.DestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationTypeSerializer
