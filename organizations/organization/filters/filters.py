import django_filters
from organizations.models import Organization


class OrganizationFilter(django_filters.FilterSet):
    degree = django_filters.CharFilter(field_name='organization_type__name', lookup_expr='icontains')
    region = django_filters.CharFilter(field_name='region__name', lookup_expr='icontains')
    education_type = django_filters.CharFilter(field_name='desc',
                                               lookup_expr='icontains')
    language = django_filters.CharFilter(field_name='locations',
                                         lookup_expr='icontains')
    class Meta:
        model = Organization
        fields = ['degree', 'region', 'education_type', 'language']
