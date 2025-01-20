from rest_framework import serializers
from organizations.models.models import Organization


class OrganizationCreateSerializer(serializers.ModelSerializer):


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
