from rest_framework import serializers

from organizations.models.organization_fields import OrganizationFields


class OrganizationFieldsListSerializersUpdate(serializers.ModelSerializer):
    description = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = OrganizationFields
        fields = ['id', 'name', 'description']
