from rest_framework import serializers
from Organization.models.models import Organization


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
        depth = 1  # This includes the related data for ForeignKey fields.


class OrganizationSerializerForLanding(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name'
        ]
