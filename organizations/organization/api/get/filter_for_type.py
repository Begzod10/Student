from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from organizations.models import Organization
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializer
from organizations.organization.filters.filter_for_organization_type import OrganizationFilter


class FilterForTypeOrganizationView(generics.ListAPIView):
    queryset = Organization.objects.filter(deleted=False).all()
    serializer_class = OrganizationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrganizationFilter
