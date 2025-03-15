from rest_framework import serializers
from organizations.models import OrganizationDegrees, OrganizationType
from organizations.organization_type.serializers.get.retrieve_view import OrganizationTypeSerializer
from rest_framework.permissions import IsAuthenticated


class OrganizationDegreesCreateUpdateSerializer(serializers.ModelSerializer):
    # organization_type = serializers.PrimaryKeyRelatedField(queryset=OrganizationType.objects.all())

    class Meta:
        model = OrganizationDegrees

        fields = ['id', 'name', 'organization_type', 'desc']

    # def create(self, validated_data):
    #     organization_type = validated_data.pop('organization_type')
    #     get_organization_type = OrganizationType.objects.get(**organization_type)
    #     return OrganizationDegrees.objects.create(**validated_data, organization_type=get_organization_type)
    #
    # def update(self, instance, validated_data):
    #     organization_type = validated_data.pop('organization_type')
    #     get_organization_type = OrganizationType.objects.get(**organization_type)
    #     instance.organization_type = get_organization_type
    #     instance.save()
    #     return instance
