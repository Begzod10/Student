from django_filters import rest_framework as filters

from organizations.models.organization_landing_page import OrganizationLandingPage


class OrganizationLandingPageFilter(filters.FilterSet):
    organization_type = filters.NumberFilter(field_name="organization__organization_type__id")
    region = filters.NumberFilter(field_name="organization__region__id")

    class Meta:
        model = OrganizationLandingPage
        fields = ['organization_type', 'region']
