from django_filters import rest_framework as filters
from organizations.models import Organization


class OrganizationFilter(filters.FilterSet):
    organization_type = filters.NumberFilter(field_name="organization_type__id")
    region = filters.NumberFilter(field_name="region__id")
    district = filters.NumberFilter(field_name='district__id')

    class Meta:
        model = Organization
        fields = ['organization_type', 'region', 'district']
