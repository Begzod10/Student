from rest_framework import serializers

from organizations.models.organization_fields import OrganizationFields


class OrganizationFieldsListSerializersUpdate(serializers.ModelSerializer):
    class Meta:
        model = OrganizationFields
        fields = '__all__'
