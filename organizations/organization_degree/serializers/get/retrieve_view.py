from rest_framework import serializers

from organizations.models.models import OrganizationDegrees


class OrganizationDegreesRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDegrees
        fields = ['id', 'name', 'organization_type']
