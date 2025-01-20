from rest_framework import serializers

from organizations.models.models import Organization
from organizations.models.organization_landing_page import OrganizationLandingPage


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'locations',
            'desc',
            'phone',
            'img',
            'organization_type',
            'region'
        ]


class OrganizationSerializerForLanding(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name'
        ]


class OrganizationHomeSerializer(serializers.ModelSerializer):
    region = serializers.CharField(source='organization.region.name', read_only=True)
    name = serializers.CharField(source='organization.name', read_only=True)
    locations = serializers.CharField(source='organization.locations', read_only=True)
    desc = serializers.CharField(source='organization.desc', read_only=True)
    phone = serializers.CharField(source='organization.phone', read_only=True)
    img = serializers.CharField(source='organization.img', read_only=True)
    organization_type = serializers.CharField(source='organization.organization_type.name', read_only=True)

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'name',
            'locations',
            'desc',
            'phone',
            'img',
            'organization_type',
            'region'
        ]

