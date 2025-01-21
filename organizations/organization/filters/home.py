from django_filters import rest_framework as filters

from organizations.models.models import Organization


class OrganizationLandingPageFilter(filters.FilterSet):
    organization_type = filters.NumberFilter(field_name="organization_type__id")
    region = filters.NumberFilter(field_name="region__id")

    class Meta:
        model = Organization
        fields = ['organization_type', 'region']
