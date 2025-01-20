from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from organizations.models import Organization
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializer
from organizations.organization.serializers.crud.create import OrganizationCreateSerializer


class OrganizationCreateApiView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = OrganizationCreateSerializer
    queryset = Organization.objects.all()
