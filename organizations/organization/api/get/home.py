from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization.filters.home import OrganizationLandingPageFilter
from organizations.organization.serializers.get.retrieve_view import OrganizationHomeSerializer


class HomeOrganizationView(generics.ListAPIView):
    queryset = OrganizationLandingPage.objects.filter(deleted=False).all()
    serializer_class = OrganizationHomeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrganizationLandingPageFilter
