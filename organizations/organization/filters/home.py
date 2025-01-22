from django_filters import rest_framework as filters

from organizations.models.models import Organization


class OrganizationLandingPageFilter(filters.FilterSet):
    organization_type = filters.NumberFilter(field_name="organization_type__id")
    region = filters.BaseInFilter(field_name="region__id")
    degree = filters.BaseInFilter(field_name="organizationlandingpage__degree__id")
    shift = filters.BaseInFilter(field_name="organizationlandingpage__shift__id")
    language = filters.BaseInFilter(field_name="organizationlandingpage__education_language__id")
    price = filters.RangeFilter(field_name="organizationlandingpage__price")

    class Meta:
        model = Organization
        fields = ['organization_type', 'region', 'degree', 'shift', 'price']
