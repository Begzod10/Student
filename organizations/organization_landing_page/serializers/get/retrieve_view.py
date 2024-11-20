from rest_framework import serializers
from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization.serializers.get.retrieve_view import OrganizationSerializerForLanding


class OrganizationLandingPageSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializerForLanding()

    class Meta:
        model = OrganizationLandingPage
        fields = [
            'id',
            'organizations',
            'year_id',
            'desc',
            'name_optional',
            'expire_date',
            'degree_id'
        ]
        depth = 1  # This will automatically include the related data for ForeignKey fields.
