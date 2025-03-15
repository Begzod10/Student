from rest_framework import serializers
from organizations.organization_type.serializers.get.retrieve_view import OrganizationTypeSerializer

from organizations.models.models import OrganizationDegrees


class OrganizationDegreesRetrieveSerializer(serializers.ModelSerializer):
    organization_type = OrganizationTypeSerializer()

    class Meta:
        model = OrganizationDegrees
        fields = ['id', 'name', 'organization_type', 'desc']
