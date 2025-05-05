from rest_framework import serializers

from organizations.models.organization_fields import OrganizationFields


class OrganizationFieldsListSerializersUpdate(serializers.ModelSerializer):
    description = serializers.CharField(allow_blank=True, required=False,source='desc')

    class Meta:
        model = OrganizationFields
        fields = ['id', 'name', 'description','organization_type','desc']
