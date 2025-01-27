from rest_framework import generics

from organizations.models import Organization
from organizations.organization.serializers.get.retrieve_view import OrganizationGrandSerializer, OrganizationDescUpdateSerializer
from organizations.organization.serializers.crud.create import OrganizationCreateSerializer

class OrganizationUpdateApiView(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationCreateSerializer


class OrganizationUpdateGrandTextApiView(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationGrandSerializer


class OrganizationUpdateDescTextApiView(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationDescUpdateSerializer
