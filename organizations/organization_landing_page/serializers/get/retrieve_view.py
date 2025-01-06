from rest_framework import serializers
from organizations.models.organization_landing_page import OrganizationLandingPage, LandingPageShift
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializerForLanding


class OrganizationLandingPageSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializerForLanding(source='organization_id')

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'organization',
            'year_id',
            'desc',
            'name_optional',
            'expire_date',
            'degree_id'
        ]
        depth = 1  # This will automatically include the related data for ForeignKey fields.


class LandingPageShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPageShift
        fields = '__all__'
        depth = 1
