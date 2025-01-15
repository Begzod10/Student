from rest_framework import serializers
from organizations.models.models import Organization, OrganizationType
from organizations.organization_type.serializers.get.retrieve_view import OrganizationTypeSerializer
from students.models.region import Region
from students.region.serializers.get.retrieve_view import RegionSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    organization_type = OrganizationTypeSerializer()
    region = RegionSerializer()

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
