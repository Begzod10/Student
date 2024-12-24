from rest_framework import serializers
from organizations.models.models import Organization, OrganizationType
from organizations.organization_type.serializers.get.retrieve_view import OrganizationTypeSerializer
from students.models.region import Region
from students.region.serializers.get.retrieve_view import RegionSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    # organization_type = serializers.PrimaryKeyRelatedField(queryset=OrganizationType.objects.all())

    # region = RegionSerializer()

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
        # depth = 1  # This includes the related data for ForeignKey fields.

    # def create(self, validated_data):
    #     organization_type_data = validated_data.pop('organization_type')
    #     region_type_data = validated_data.pop('region')
    #     organization_type = OrganizationType.objects.get(**organization_type_data)
    #     region = Region.objects.get(**region_type_data)
    #     organization = Organization.objects.create(**validated_data,
    #                                                organization_type=organization_type,
    #                                                region=region)  # Create parent object
    #
    #     return organization
    #
    # def update(self, instance, validated_data):
    #     organization_type_data = validated_data.pop('organization_type')
    #     region_type_data = validated_data.pop('region')
    #     organization_type = OrganizationType.objects.get(**organization_type_data)
    #     region = Region.objects.get(**region_type_data)
    #     instance.organization_type = organization_type
    #     instance.region = region
    #     instance.save()
    #     return instance  # Return the updated instance


class OrganizationSerializerForLanding(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name'
        ]
