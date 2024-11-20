from organizations.models.models import OrganizationDegrees
from rest_framework import serializers


class OrganizationDegreesRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDegrees
        fields = ['id','name','organization_type']
