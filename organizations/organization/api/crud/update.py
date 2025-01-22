from rest_framework import generics

from organizations.models import Organization
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializer, \
    OrganizationGrandSerializer, OrganizationDescSerializer


class OrganizationUpdateApiView(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationUpdateGrandTextApiView(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationGrandSerializer


class OrganizationUpdateDescTextApiView(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationDescSerializer
