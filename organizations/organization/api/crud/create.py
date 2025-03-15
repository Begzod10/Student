from rest_framework import generics

from organizations.models import Organization
from organizations.organization.serializers.crud.create import OrganizationCreateSerializer


class OrganizationCreateApiView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = OrganizationCreateSerializer
    queryset = Organization.objects.all()
