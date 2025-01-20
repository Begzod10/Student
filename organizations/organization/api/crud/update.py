from rest_framework import generics

from organizations.models import Organization
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializer


class OrganizationUpdateApiView(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


